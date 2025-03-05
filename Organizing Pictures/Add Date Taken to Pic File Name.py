import os
from datetime import datetime
from exif import Image as ExifImage
from pillow_heif import register_heif_opener, open_heif

register_heif_opener()

def get_date_taken(file_path):
    try:
        if file_path.lower().endswith('.jpeg'):
            with open(file_path, 'rb') as image_file:
                image = ExifImage(image_file)
                if image.has_exif and image.datetime_original:
                    return datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
        elif file_path.lower().endswith('.heic'):
            heif_file = open_heif(file_path)
            exif_data = heif_file.info.get('exif', {})
            if 'DateTimeOriginal' in exif_data:
                return datetime.strptime(exif_data['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Error reading date taken from {file_path}: {e}")
    return None

def append_date_taken_to_filename(picture_dir):
    
    for file_name in os.listdir(picture_dir):
        if file_name.lower().endswith(('.jpeg', '.heic')):
            file_path = os.path.join(picture_dir, file_name)
            date_taken = get_date_taken(file_path)
            
            if date_taken:
                date_str = date_taken.strftime('%Y-%m-%d')
                base, extension = os.path.splitext(file_name)
                new_file_name = f"{date_str}_{base}{extension}"
                new_file_path = os.path.join(picture_dir, new_file_name)
                
                if not os.path.exists(new_file_path):
                    os.rename(file_path, new_file_path)
                else:
                    print(f"File {new_file_name} already exists. Skipping.")

if __name__ == "__main__":
    picture_dir = r"D:\__\Rename these" # os.getcwd()
    append_date_taken_to_filename(picture_dir)
    print("Done")

# This currently doesn't work for HEIC files. 
# Error reading date taken from D:\__\IMG_0702.HEIC: a bytes-like object is required, not 'str'