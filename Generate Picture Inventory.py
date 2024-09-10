import os
from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd

# Define the output file path
output_file = 'Picture Inventory.xlsx'

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

# Collect data
data = []

# Traverse the directory tree
for root, dirs, files in os.walk('./Pictures'):
    for file in files:

        # Get the full file path
        full_path = os.path.join(root, file)
        date_taken = get_date_taken(full_path)

        # Append the data to the list
        data.append([full_path, file, date_taken])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Full Path (link to file directory)', 'File Name (link to the file)', 'Date Taken'])

# Write the DataFrame to an Excel file with hyperlinks
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, startrow=0)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    # rename the sheet
    worksheet.title = 'Picture Inventory'
    
    # Add hyperlinks to the first column
    for row_num, full_path in enumerate(df.iloc[:, 0], start=2):
        directory_path = os.path.dirname(full_path)
        worksheet.write_url(f'A{row_num}', directory_path, string=full_path)
        worksheet.write_url(f'B{row_num}', full_path, string=df.iloc[row_num-2, 1])

print('Done!')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Old code... 

# https://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil
# https://stackoverflow.com/questions/44636152/how-to-modify-exif-data-in-python

# # Scan through pix 
# #   -> read attributes and write to excel 
# # Also want to be able to set a certain attribute(s) in a given folder

# # https://medium.com/geekculture/extract-exif-data-from-photos-using-python-440e598274f1 

# import os

# from PIL import Image

# # # Loop thru pix in dir
# # rootdir = r"D:\Pictures, Videos, Movies\Vehicles\Mustang"

# # # loop thru all files
# # with os.scandir(rootdir) as entries:
# #     for entry in entries:
# #         print(entry.stat())

# img = Image.open(r'D:\Pictures, Videos, Movies\Vehicles\Mustang\1967mustangcp121503 - NOT MY CAR.jpg')
# exif_data = img.getexif()