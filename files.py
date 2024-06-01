file_path="./app.js"
open_file= open(file_path, "r")
print(open_file)
line = open_file.readlines()
print(line)
print(len(line))
