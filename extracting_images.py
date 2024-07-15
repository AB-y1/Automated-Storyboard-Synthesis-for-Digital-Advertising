import os
import shutil

def copy_files_to_new_dir(source_dir, dest_dir):
    """
    Copies files from folders in the source directory to a new directory.

    Args:
        source_dir (str): The path to the source directory containing the folders.
        dest_dir (str): The path to the destination directory where the files will be copied.
    """
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through the folders in the source directory
    for folder_name in os.listdir(source_dir):
        source_folder = os.path.join(source_dir, folder_name)
        
        # Check if the item is a directory
        if os.path.isdir(source_folder):
            # Copy the files from the folder to the destination directory
            for filename in os.listdir(source_folder):
                source_file = os.path.join(source_folder, filename)
                dest_file = os.path.join(dest_dir, filename)
                shutil.copy2(source_file, dest_file)
                print(f"Copied file: {filename}")
        else:
            print(f"Skipping non-directory: {folder_name}")

best_Assests_dir = "src/best_Assests"
image_dest_dir = "src/image"
copy_files_to_new_dir(best_Assests_dir, image_dest_dir)