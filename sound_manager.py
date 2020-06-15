import os
import random
from pathlib import Path
import subprocess


def get_sound_files():
    current_directory = os.getcwd()
    sound_folder = os.path.join(current_directory, 'sounds')
    path_object = Path(sound_folder)
    sound_list = []
    for file in path_object.glob('*.mp3'):
        sound_list.append(file)
    return sound_list


def play_sound():
    sound_list = get_sound_files()
    sound_file = random.choice(sound_list)
    subprocess.Popen(['open', sound_file])
