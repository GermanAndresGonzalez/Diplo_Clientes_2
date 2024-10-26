import os

# Suppose you have a file path
file_path = "/home/user/file.txt"

# Get the directory name of the file
dir_name = os.path.dirname(file_path)

# New directory to add
new_dir = "new_directory"

# Combine the directory name with the new directory
new_path = os.path.join(dir_name, new_dir)


print(new_path)

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
print("Segundo print\n", BASE_DIR, "\n")

ruta = BASE_DIR + ("/datos/")
print(ruta)
