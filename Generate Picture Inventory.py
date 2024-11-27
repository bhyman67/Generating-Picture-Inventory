import os
from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd

# +++++++++++++++++++++++++++++++++++++++++  UDF  +++++++++++++++++++++++++++++++++++++++++

def get_date_taken(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'DateTimeOriginal':
                    return value
    except Exception as e:
        pass
    return 'Unknown'

# ++++++++++++++++++++++++++++++++++++++++  Script  ++++++++++++++++++++++++++++++++++++++++

# Define the output file path
output_file = os.path.join(os.pardir, 'Picture Inventory.xlsx')

# Collect data
data = []

# Traverse the directory tree to grab the file paths
for root, dirs, files in os.walk(os.path.join(os.pardir, 'Pictures')):
    for file in files:

        # Get the full file path
        full_path = os.path.abspath(os.path.join(root, file))
        date_taken = get_date_taken(full_path)

        # Extract the top-level folder
        relative_path = os.path.relpath(full_path, os.path.join(os.pardir, 'Pictures'))
        top_level_folder = relative_path.split(os.sep)[0]

        # Append the data to the list
        data.append([full_path, file, date_taken, top_level_folder])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Full Path (link to file directory)', 'File Name (link to the file)', 'Date Taken', 'Top Level Folder'])

# Write the DataFrame to an Excel file with hyperlinks
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:

    df.to_excel(writer, index=False, startrow=0)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.title = 'Picture Inventory'
    
    # Add hyperlinks to the first column
    for row_num, full_path in enumerate(df.iloc[:, 0], start=2):
        directory_path = os.path.dirname(full_path)
        worksheet.write_url(f'A{row_num}', directory_path, string=full_path)
        worksheet.write_url(f'B{row_num}', full_path, string=df.iloc[row_num-2, 1])

input('Done!')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Some concepts to understand:

# EXIF stands for ‘Exchangeable Image File Format’
#   -> a standard for storing metadata in image files

# pillow python library for extracting exif data from images

# https://medium.com/geekculture/extract-exif-data-from-photos-using-python-440e598274f1 