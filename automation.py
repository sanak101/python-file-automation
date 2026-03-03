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

    
# Renaming file with a prefix

'''for file in os.listdir(folder):
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, "new_" + file)

    os.rename(old_path, new_path)'''



for index, file in enumerate(os.listdir(folder1)):
    extension = file.split(".")[-1]
    new_name = f"image_{index}.{extension}"

    os.rename(
        os.path.join(folder1, file),
        os.path.join(folder1, new_name)

    )

for file in os.listdir(folder):
    if file.startswith("new_"):
        old_path = os.path.join(folder, file)

        original_name = file.replace("new_", "", 1)
        new_path = os.path.join(folder, original_name)

        os.rename(old_path, new_path)

print("Files restored.")