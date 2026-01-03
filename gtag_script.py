import os
import time
import shutil
import subprocess
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw
from nextcord import SyncWebhook, File

from image_slicer import ImageSlicer
import cv2 # pip install opencv-python (ps, it worked)

from guizero import App, Text, PushButton, Picture, Box, TextBox
import tkinter as tk
import webbrowser

import math
import threading # chatgpt pls work

## old_directory = r"C:\Users\paz\Desktop\gtag_export\obamahavedih"
## new_directory = r"C:\Users\paz\Desktop\gtag_export\g"
## update_directory = r"C:\Users\paz\Desktop\g\last"
##version_dir = f"{new_directory}\ExportedProject\ProjectSettings\ProjectVersion.txt"
##with open(version_dir) as file:
##        version = file.read()

## make shit work later ^ ^ ^ ^ ^ 


def discord():
    webbrowser.open_new_tab("https://discord.gg/ZtGqq2wfFc")

def want_dir(thing):
    global old_directory, update_directory, new_directory
    if thing == "old":
        old_dir = filedialog.askdirectory(title="select the gtag export made BEFORE the newest update:")
        olddir_shower.value = old_dir
        olddir_shower.tk.config(state="readonly", readonlybackground="#0F0E0F")

        old_directory = old_dir
    elif thing == "update":
        update_dir = filedialog.askdirectory(title="select where you want the latest files to be dumped to:")
        export_shower.value = update_dir
        export_shower.tk.config(state="readonly", readonlybackground="#0F0E0F")

        update_directory = update_dir
    elif thing == "new":
        new_dir = filedialog.askdirectory(title="select the export of the NEWEST gtag update:")
        new_shower.value = new_dir
        new_shower.tk.config(state="readonly", readonlybackground="#0F0E0F")

        new_directory = new_dir

def bro_just_typin_shit_lmao(text):
    command_ting.tk.config(state="normal")
    current = command_ting.value.rstrip("\n") # i prefer to not use ai btw half of this lib is undocumented scooby doo type shit

    if current:
        command_ting.value = current + "\n" + text
    else:
        command_ting.value = text

    command_ting.tk.config(state="disabled")
    command_ting.tk.see("end")

def threading_bullshit():
    threading.Thread(target=start_export).start()

def start_export():
    version = "6000.2.9f1"
    bbno = version.upper()
    texture = 0
    sprite = 0
    audio = 0
    mesh = 0

    ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ## TEXTURE2D ##

    old_Texture2D = f"{old_directory}/ExportedProject/Assets/Texture2D"
    new_Texture2D = f"{new_directory}/ExportedProject/Assets/Texture2D"
    old_Texture2D_files = {f for f in os.listdir(old_Texture2D) if f.endswith(".png")} # filters anoying .png.meta duplicate files
    new_Texture2D_files = {f for f in os.listdir(new_Texture2D) if f.endswith(".png")}

    updated_Texture2D_files = new_Texture2D_files - old_Texture2D_files

    # if not os.path.exists(f"{update_directory}/Texture2D"): # no path check just for sure
    os.makedirs(f"{update_directory}/Texture2D")
    os.makedirs(f"{update_directory}/Texture2DArray")
    os.makedirs(f"{update_directory}/Mesh")
    os.makedirs(f"{update_directory}/AudioClip")

    for file_name in updated_Texture2D_files:
        src_path = os.path.join(new_Texture2D, file_name)
        dst_path = os.path.join(f"{update_directory}/Texture2D", file_name)
        shutil.copy2(src_path, dst_path)
        bro_just_typin_shit_lmao(f"Dumped Texture2D: {file_name}")
        texture = texture + 1

    bro_just_typin_shit_lmao("Finished dumping all Texture2D files!")
    time.sleep(0.5)

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
        bro_just_typin_shit_lmao(f"Dumped AudioClip: {file_name}")
        audio = audio + 1

    bro_just_typin_shit_lmao("Finished dumping all AudioClip files!")
    time.sleep(0.5)

    ## Mesh ## Mesh ## Mesh ## Mesh ## Mesh ## Mesh ## Mesh ##

    old_Mesh = f"{old_directory}/ExportedProject/Assets/Mesh"
    new_Mesh = f"{new_directory}/ExportedProject/Assets/Mesh"
    old_Mesh_files = {f for f in os.listdir(old_Mesh) if f.endswith(".asset")}
    new_Mesh_files = {f for f in os.listdir(new_Mesh) if f.endswith(".asset")}

    updated_Mesh_files = new_Mesh_files - old_Mesh_files

    for file_name in updated_Mesh_files:
        src_path = os.path.join(new_Mesh, file_name)
        dst_path = os.path.join(f"{update_directory}/Mesh", file_name)
        shutil.copy2(src_path, dst_path)
        bro_just_typin_shit_lmao(f"Dumped Mesh: {file_name}")
        mesh = mesh + 1

    bro_just_typin_shit_lmao("Finished dumping all Mesh files!")
    time.sleep(0.5)

    ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ## Texture2DArray ##

    def Slice_Texture2DArray(image_path, output_path):
        slicer = ImageSlicer(image_path)
        hpx, wpx = slicer.height, slicer.width

        if wpx/hpx == 1:
            bro_just_typin_shit_lmao("Some sprites are same size so they wont be sliced")
        else:
            bro_just_typin_shit_lmao(f"Slicing {math.floor(hpx/wpx)} images from sprite")
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
        sprite = sprite + 1

    bro_just_typin_shit_lmao("Finished slicing Texture2DArray files!")
    bro_just_typin_shit_lmao("")
    bro_just_typin_shit_lmao("the whole ting is doen now")
    bro_just_typin_shit_lmao("you can now close the program!")

window = App(title="discord.gg/ZtGqq2wfFc", height=500, width=750, bg="#131214")
window.tk.iconphoto(False, tk.PhotoImage(file="fuckass\\miniicon.png")) #slicing images doesnt work at python 3.11.9+ so i have to do this fuckass shit
window.tk.resizable(False, False)

# spinny
spinny_container = Box(window, align="top", width="fill", height=100) # go to top
spinny = Picture(spinny_container, image="fuckass\\output-onlinegiftools.gif", align="left", height=100, width=100) # go to left in container
text = Picture(spinny_container, image="fuckass\\text.png", align="left", height=50, width=500)

#discord link
discord_container = Box(window, align="bottom", width="fill", height=15) # go to botom
discord_link = PushButton(discord_container, image="fuckass\\discordiolink.png", height=15, width=115, align="right", command=discord)

# old
olddir_container = Box(window, align="top", width=700, height=30)
olddir_button = PushButton(olddir_container, height=30, width=10, align="left", text="PreLast Directory", command=lambda: want_dir("old"))
olddir_button.tk.config(fg="white")
olddir_shower = TextBox(olddir_container, height=500, width=50,align="left")
olddir_shower.tk.config(font=("TkDefaultFont", 16))  # font family + size
olddir_shower.tk.config(fg="white", bg="#000000")
#old
#new
new_container = Box(window, align="top", width=700, height=30)
new_button = PushButton(new_container, height=30, width=10, align="left", text="Latest Directory", command=lambda: want_dir("new"))
new_button.tk.config(fg="white")
new_shower = TextBox(new_container, height=500, width=50,align="left")
new_shower.tk.config(font=("TkDefaultFont", 16))  # font family + size
new_shower.tk.config(fg="white", bg="#000000")
#new
#export
export_container = Box(window, align="top", width=700, height=30)
export_button = PushButton(export_container, height=30, width=10, align="left", text="Where To Export", command=lambda: want_dir("update"))
export_button.tk.config(fg="white")
export_shower = TextBox(export_container, height=500, width=50,align="left")
export_shower.tk.config(font=("TkDefaultFont", 16))  # font family + size
export_shower.tk.config(fg="white", bg="#000000")
#export

#exprt bttn
start_export_button = PushButton(window, align="top", height=29, width=97, image="fuckass\\emy.png", command=threading_bullshit)

export_shower.tk.config(state="readonly", readonlybackground="#0F0E0F")
new_shower.tk.config(state="readonly", readonlybackground="#0F0E0F")
olddir_shower.tk.config(state="readonly", readonlybackground="#0F0E0F")

command_ting = TextBox(window, align="bottom", width=70, height=50, multiline=True)
command_ting.tk.config(state="disabled", bg="#0F0E0F", fg="white")

bro_just_typin_shit_lmao("made by paztv at discord.gg/ZtGqq2wfFc")

window.display()