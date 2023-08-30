import re
import os
import language_tool_python as lt

def print_progress_bar(completed, total, length=50):
    progress = int(length * completed / total)
    bar = "#" * progress + "-" * (length - progress)
    print(f"\r[{bar}] {completed}/{total} ({100*completed/total:.2f}%)", end='')

def check_grammar(text, tool):
    corrected_text = tool.correct(text)
    return corrected_text

def write_and_split_paragraph(paragraph, outfile, tool):
    paragraph = re.sub(r'\s+', ' ', paragraph).strip()
    sentences = re.split(r'(?<=\.)\s|(?<=\?)\s|(?<=\!)\s', paragraph)
    
    current_subparagraph = ""
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        sentence_length = len(sentence)
        
        if current_length + sentence_length + 1 > 2500:
            corrected_subparagraph = check_grammar(current_subparagraph, tool)
            outfile.write(corrected_subparagraph.strip() + '\n\n')
            current_subparagraph = ""
            current_length = 0
            
        current_subparagraph += sentence + " "
        current_length += sentence_length + 1
    
    if current_subparagraph:
        corrected_subparagraph = check_grammar(current_subparagraph, tool)
        outfile.write(corrected_subparagraph.strip() + '\n\n')

current_paragraph = ""
tool = lt.LanguageTool('en-US')

input_file_path = 'form.txt'
output_file_path = 'translate.txt'

total_size = os.path.getsize(input_file_path)
read_size = 0

with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        line = line.rstrip()
        line = re.sub(r' {1,}\d+$', '', line)
        
        read_size += len(line.encode('utf-8'))
        print_progress_bar(read_size, total_size)
        
        if re.match(r' {3,}[A-Z]', line):
            if current_paragraph:
                write_and_split_paragraph(current_paragraph, outfile, tool)
            current_paragraph = line.lstrip()
        else:
            current_paragraph += " " + line.lstrip()

    if current_paragraph:
        write_and_split_paragraph(current_paragraph, outfile, tool)

print("\nProcessing complete.")
