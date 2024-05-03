file_path = "C:\\users\\admin\\file4.txt"
count_path = "C:\\users\\admin\\line_count.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

line_count = len(lines)

with open(count_path, 'w') as count_file:
    count_file.write(f"The file has {line_count} lines.")
