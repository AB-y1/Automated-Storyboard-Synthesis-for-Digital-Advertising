import os
import shutil

# Set the source and destination directories
source_dir = "data/Archive-last/Challenge_Data/Assets"
dest_dir = "best_Assests2"

# the path that containing the names of best 100 assest's folders 
assets_names = "src/assests_names.txt"

# Read the folder names from the text file
with open(assets_names, "r") as f:
    folder_names = [line.strip() for line in f]

# # Create the destination directory if it doesn't exist
# if not os.path.exists(dest_dir):
#     os.makedirs(dest_dir)

# Copy the folders from the source directory to the destination directory
for folder_name in folder_names:
    source_folder = os.path.join(source_dir, folder_name)
    dest_folder = os.path.join(dest_dir, folder_name)
    
    if os.path.exists(source_folder):
        if not os.path.exists(dest_folder):
            shutil.copytree(source_folder, dest_folder)
            print(f"Copied folder: {folder_name}")
        else:
            print(f"Destination folder already exists: {folder_name}")
    else:
        print(f"Source folder not found: {folder_name}")



