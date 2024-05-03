# with b flag, we can read binary files
# we can combine b flag with r flag to read binary files

with open('images/lama.jpg', 'rb') as bin_file:
    bin_data = bin_file.read()
    print(bin_data)
