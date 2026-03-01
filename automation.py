import os

# use a raw string so backslashes aren’t interpreted as escape sequences
folder = r"c:\Users\User\OneDrive\Documents\python-tutorials"
files = os.listdir(folder)

for file in files:
    print(file)

print("total files", len(files))

# Practice tasks

for file in files:
    if file.endswith(".txt"):
        print(file)

folder1 = r"C:\Users\User\OneDrive\Pictures"
files1 = os.listdir(folder1)

for file in files1:
    if file.endswith(".png"):
        print(file)


os.path.join(folder, "file.txt")
os.path.isfile(r"C:\Users\User\OneDrive\Documents\python-tutorials\file.txt")
os.path.isdir(r"C:\Users\User\OneDrive\Documents\python-tutorials")

for file in os.listdir(folder):
    full_path = os.path.join(folder, file)

    if os.path.isfile(full_path):
        print("File:", file)
    else:
        print("Folder:", file)

        