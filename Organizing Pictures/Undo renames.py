import os
import re

def remove_duplicate_date():

    current_directory = os.getcwd()
    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})_(.*\.jpeg)$', re.IGNORECASE)
    
    for file_name in os.listdir(current_directory):

        match = pattern.match(file_name)
        if match and match.group(1) == match.group(2):

            new_file_name = f"{match.group(2)}_{match.group(3)}"
            old_file_path = os.path.join(current_directory, file_name)
            new_file_path = os.path.join(current_directory, new_file_name)
            
            if not os.path.exists(new_file_path):
                os.rename(old_file_path, new_file_path)
            else:
                print(f"File {new_file_name} already exists. Skipping.")

if __name__ == "__main__":
    
    remove_duplicate_date()
    print("Done with renaming.")