from datetime import datetime, timedelta
import os
import pyexiv2 as ex

"""
Install python-exiv2
It's a modul to read image metadata.
"""
# Problem: I have multiple sources of pictures of one vacancy trip and want to show them in order.

path = os.getcwd()

"""
For every file in the current directory,
get the Time the photo got shot from the metadata.
You take the date and time and rename every file in the folder starting with the date and time.
"""

cur_file_name = os.path.basename(__file__)

def bycanon(metadata):
    # Metadata must be loaded here
    text = 'Canon'
    # load type of camera
    camera = metadata['Exif.Image.Make']
    if text == camera.value:
        return True
    else:
        return False



def finde_bindestrich(filename_old, string_datetime):
    """
    It could have happended that some files are already renamed
    with the date and time in the front.
    If the file got already renamed, the part of the name until the 
    first occurence of '_' must be the date and time of the metadata.
    """
    file = str(filename_old)
    strich = '_'
    wo_ist_strich = file.find(strich)
    string_compare = file[:wo_ist_strich]
    if string_compare == string_datetime:
        return True
    else:
        return False


for file in os.listdir(path):
    if file != cur_file_name:
        # When there's not metadata, go to the next file.
        try:
            metadata = ex.ImageMetadata(file)
            metadata.read()
            tag = metadata['Exif.Image.DateTime']
            zeit = tag.value
        except Exception:
            continue

# I didn't change the time zone of the camera so I have to adjust it.

        if bycanon(metadata) is True:
            timediff = tag.value + timedelta(hours=5)
            zeit = str(timediff)
        else:
            zeit = zeit

        if finde_bindestrich(file, zeit) is False:
            print(file)
            os.rename(file, str(zeit) + '_' + file)

