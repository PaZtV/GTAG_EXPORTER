import os
import time
import shutil
from tkinter import filedialog

from image_slicer import ImageSlicer
import cv2 # pip install opencv-python

print("Please select the directory of the LAST gorilla tag export")
old_directory = filedialog.askdirectory(title="Select OLD gtag export")
print(f"Selected: {old_directory}")

print("Please select the directory of the NEWEST gorilla tag export")
new_directory = filedialog.askdirectory(title="Select NEW gtag export")
print(f"Selected: {new_directory}")

print("Please select the directory to copy the new files to")
update_directory = filedialog.askdirectory(title="Select folder to copy new files to")
print(f"Selected: {update_directory}")

# old_directory = r"C:\Users\paz\Desktop\gtag_export\obamahavedih"
# new_directory = r"C:\Users\paz\Desktop\gtag_export\11.28.2025"
# update_directory = r"C:\Users\paz\Desktop\GTAG_EXPORTER\farted"

## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ##

old_Texture2D = f"{old_directory}/ExportedProject/Assets/Texture2D"
new_Texture2D = f"{new_directory}/ExportedProject/Assets/Texture2D"
old_Texture2D_files = {f for f in os.listdir(old_Texture2D) if f.endswith(".png")} # filters anoying .png.meta duplicate files
new_Texture2D_files = {f for f in os.listdir(new_Texture2D) if f.endswith(".png")}

updated_Texture2D_files = new_Texture2D_files - old_Texture2D_files

if not os.path.exists(f"{update_directory}/Texture2D"): # no path check just for sure
    os.makedirs(f"{update_directory}/Texture2D")
    os.makedirs(f"{update_directory}/Texture2DArray")
    os.makedirs(f"{update_directory}/Mesh")
    os.makedirs(f"{update_directory}/AudioClip")

for file_name in updated_Texture2D_files:
    src_path = os.path.join(new_Texture2D, file_name)
    dst_path = os.path.join(f"{update_directory}/Texture2D", file_name)
    shutil.copy2(src_path, dst_path)
    print(f"Copied Texture2D: {file_name}")

## AudioClip ## AudioClip ## AudioClip ## AudioClip ## AudioClip ## AudioClip ## AudioClip ##

old_Audio = f"{old_directory}/ExportedProject/Assets/AudioClip"
new_Audio = f"{new_directory}/ExportedProject/Assets/AudioClip"
old_Audio_files = {f for f in os.listdir(old_Audio) if f.endswith(".ogg")}
new_Audio_files = {f for f in os.listdir(new_Audio) if f.endswith(".ogg")}

updated_Audio_files = new_Audio_files - old_Audio_files

for file_name in updated_Audio_files:
    src_path = os.path.join(new_Audio, file_name)
    dst_path = os.path.join(f"{update_directory}/AudioClip", file_name)
    shutil.copy2(src_path, dst_path)
    print(f"Copied AudioClip: {file_name}")

## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ##

def Slice_Texture2DArray(image_path, output_path):
    slicer = ImageSlicer(image_path)
    hpx, wpx = slicer.height, slicer.width

    if wpx/hpx == 1:
        print(f"Some sprites are same size so they will be skipped")
    else:
        print(f"Slicing {hpx/wpx} images from sprite")

        slicer.slice( # slices image
            output_dir=output_path,
            tile_width=wpx,
            tile_height=wpx,
            naming_format="tile_{row}.png"
        )

Texture2DArrays = f"{new_directory}/ExportedProject/Assets/Texture2DArray"
Texture2DArray_files = {f for f in os.listdir(Texture2DArrays) if f.endswith(".png")} # filters duplicate files

for file_name in Texture2DArray_files:

    good_file_name = file_name.replace('TexArrayAtlas_', '')

    src_path = os.path.join(Texture2DArrays, file_name)
    dst_path = os.path.join(f"{update_directory}/Texture2DArray", good_file_name)
    Slice_Texture2DArray(src_path, dst_path)