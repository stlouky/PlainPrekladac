import language_tool_python as lt
import os

def print_progress_bar(completed, total, length=50):
    progress = int(length * completed / total)
    bar = "#" * progress + "-" * (length - progress)
    print(f"\r[{bar}] {completed}/{total} ({100*completed/total:.2f}%)", end='')

def check_czech_grammar(input_file, output_file):
    tool = lt.LanguageTool('cs-CZ')
    
    total_size = os.path.getsize(input_file)
    read_size = 0
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            corrected_line = tool.correct(line)
            outfile.write(corrected_line)
            
            read_size += len(line.encode('utf-8'))
            print_progress_bar(read_size, total_size)

    print("\nProcessing complete.")

if __name__ == '__main__':
    input_file = 'translate.txt'  # předpokládaný název výsledného souboru po předchozím zpracování
    output_file = 'prelozeno.txt'  # název souboru po gramatické kontrole
    check_czech_grammar(input_file, output_file)
