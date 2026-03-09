import os
import shutil

folder = input("Enter folder path:")

moved_files = 0

for file in os.listdir(folder):
    full_path = os.path.join(folder,file)

    if os.path.isfile(full_path):
        extension = file.split(".")[-1]
        target = os.path.join(folder, extension)

        if not os.path.exists(target):
            os.mkdir(target)

        shutil.move(full_path,os.path.join(target,file))
        moved_files += 1

print("Total moved files:", moved_files)