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
        