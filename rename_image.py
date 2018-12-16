import os
import pyexiv2 as ex

"""
Install python-exiv2
It's a modul to read image metadata.
"""


path = os.getcwd()

"""
For every file in the current directory,
get the Time the photo got shot from the metadata.
You take the date and time and rename every file in the folder starting with the date and time.
"""

cur_file_name = os.path.basename(__file__)

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
        metadata = ex.ImageMetadata(file)
        metadata.read()
        tag = metadata['Exif.Image.DateTime']
        zeit = tag.raw_value
        if finde_bindestrich(file, zeit) is False:
            os.rename(file, zeit + '_' + file)

