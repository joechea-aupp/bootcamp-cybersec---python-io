file_path = "C:\\users\\admin\\file5.txt"
reversed_path = "C:\\users\\admin\\reversed.txt"

with open(file_path, 'r') as file:
    content = file.read()

reversed_content = content[::-1]

with open(reversed_path, 'w') as reversed_file:
    reversed_file.write(reversed_content)
