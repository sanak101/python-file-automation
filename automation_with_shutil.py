import os
import shutil

folder = r"C:\Users\User\OneDrive\Documents\python-tutorials"
files = os.listdir(folder)


for file in os.listdir(folder):
    if file.endswith(".jpg"):
        shutil.move(
            os.path.join(folder, file),
            os.path.join("images", file)
        )

# shutil.copy(source_path, destination_path)
source_folder = r"C:\Users\User\OneDrive\Documents\python-tutorials"
destination_folder =  r"C:\Users\User\OneDrive\Pictures"

for file in os.listdir(source_folder):
    full_path = os.path.join(source_folder, file)

    if os.path.isfile(full_path):
        shutil.copy(full_path, destination_folder)
        

