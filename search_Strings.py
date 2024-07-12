import os
import subprocess

def search_files(directory, search_string):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                if file_name.lower().endswith('.dll') or file_name.lower().endswith('.lib') or file_name.lower().endswith('.bin') or file_name.lower().endswith('.dat'):  
                    try:
                        output = subprocess.check_output(['strings', file_path ], universal_newlines=True)
                        lines = output.splitlines()
                        for line_number, line in enumerate(lines, 1):
                            #print(line)
                            if search_string in line:
                                print(f'Found in file: {file_path}, line {line_number}:')
                                print(line.strip())
                    except subprocess.CalledProcessError as e:
                        print(f'Error running strings command on file: {file_path}, {e}')
                elif file_name.lower().endswith('.pak'):
                    continue
                else:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            for line_number, line in enumerate(file, 1):
                                if search_string in line:
                                    print(f'Found in file: {file_path}, line {line_number}:')
                                    print(line.strip())
                    except Exception as e:
                        print(f'Error reading file: {file_path}, {e}')

if __name__ == "__main__":
    directory_to_search = '/home/xxx/foldertocheck'
    string_to_find = 'sqlite_version'
    search_files(directory_to_search, string_to_find)
