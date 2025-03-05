import os
import shutil

# Move all files from subdirectories to the current directory

def move_files_to_current_directory():
    current_directory = os.getcwd()
    
    for root, dirs, files in os.walk(current_directory):
        if root == current_directory:
            continue
        
        for file in files:
            source = os.path.join(root, file)
            destination = os.path.join(current_directory, file)
            
            if not os.path.exists(destination):
                shutil.move(source, destination)
            else:
                print(f"File {file} already exists in the current directory. Skipping.")

if __name__ == "__main__":
    move_files_to_current_directory()
    print("Done")