source_path = "C:\\users\\admin\\source.txt"
destination_path = "C:\\users\\admin\\destination.txt"

with open(source_path, 'r') as source_file:
    content = source_file.read()

with open(destination_path, 'w') as dest_file:
    dest_file.write(content)
