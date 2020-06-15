#! /usr/local/bin/python3


# shows a daily reminder. gets data from daily_reminders_module
# use subprocess. Popen to open file with default program
# plays an ambient noise just for fun

import os
import random
import daily_reminders_module
from pathlib import Path
import subprocess




import logging
logging.basicConfig(level=logging.DEBUG)

#Put this line where you want to see if there's an error
logging.debug('The Log message.')
# eg., logging.debug(type(first))

# put this line in to disable logging messages
logging.disable(logging.CRITICAL)


def get_sound_files():
    currentDirectory = os.getcwd()
    soundFolder = os.path.join(currentDirectory, 'sounds')
    pathObject = Path(soundFolder)
    soundList = []
    for file in pathObject.glob('*.mp3'):
        soundList.append(file)
    return soundList

def play_sound():
    sound_list = get_sound_files()
    soundfile = random.choice(sound_list)
    subprocess.Popen(['open', soundfile])
play_sound()


def random_color():
    colors = "red blue green purple gray brown navy orange orchid4"
    colorList = colors.split()
    return random.choice(colorList)



from tkinter import *

class myGUI:

    def display_finish_button(self):
        self.quitButton.pack(side=TOP, fill=X)

    def command_j(self):
        play_sound()
        todays_reminder = daily_reminders_module.get_todays_data("./dailyjapan.txt")
        self.label.config(fg=random_color(), text=todays_reminder)


    def command_c(self):
        play_sound()
        todays_reminder = daily_reminders_module.get_todays_data("./dailychinese.txt")
        self.label.config(fg=random_color(), text=todays_reminder)

    def command_p(self):
        play_sound()
        todays_reminder = daily_reminders_module.get_todays_data("./dailypython.txt")
        self.label.config(fg=random_color(), text=todays_reminder)

    def command_l(self):
        play_sound()
        todays_reminder = daily_reminders_module.get_todays_data("./dailylinux.txt")
        self.label.config(fg=random_color(), text=todays_reminder)

    def command_r(self):
        play_sound()
        todays_reminder = daily_reminders_module.get_todays_data("./dailyrom.txt")
        self.label.config(fg=random_color(), text=todays_reminder)

    def __init__(self, master):
        # This is called automatically when you create the instance of the class. Master means the root or main window.
        frame = Frame(master)
        frame.pack(expand=YES, fill=BOTH)
        # when you create a button you must make it equal self

        # label
        todays_reminder = daily_reminders_module.display_one()
        self.label = Label(frame, text=todays_reminder, height=10, width=90, bg="black", fg=random_color(),
                           font="Arial 40")
        self.label.pack(expand=YES, fill=BOTH)

        self.Button_j = Button(frame, text="japanese", bg='blue', font="Arial 25", command=self.command_j)
        self.Button_j.pack(expand=YES, fill=BOTH)

        self.Button_c = Button(frame, text="chinese", bg='blue', font="Arial 25", command=self.command_c)
        self.Button_c.pack(expand=YES, fill=BOTH)

        self.Button_p = Button(frame, text="python", bg='blue', font="Arial 25", command=self.command_p)
        self.Button_p.pack(expand=YES, fill=BOTH)

        self.Button_l = Button(frame, text="linux", bg='blue', font="Arial 25", command=self.command_l)
        self.Button_l.pack(expand=YES, fill=BOTH)

        self.Button_r = Button(frame, text="romanian", bg='blue', font="Arial 25", command=self.command_r)
        self.Button_r.pack(expand=YES, fill=BOTH)

        # the function doesn't have a (), because you're not calling it. just assigning it.
        self.nextButton = Button(frame, text="next", bg='blue', font="Arial 25", command=self.change_display)
        self.nextButton.pack(side=TOP, fill=X)

        # built in quit function
        self.n = 0
        self.quitButton = Button(frame, text="finish and close", bg='blue', font="Arial 25", command=frame.quit)
        self.quitButton.pack(side=TOP, fill=X)

    def change_display(self):
        """ refresh the content of the label every second """
        play_sound()
        todays_reminder = daily_reminders_module.display_one()


        self.label.config(fg=random_color(), text=todays_reminder)
        self.n += 1




    def clear_display(self):
        self.label.configure(text="", fg="green")


window = Tk()
window.title("daily reminder - 每日提醒 - momento zilnic")
# now create an instance of the class
classWindow = myGUI(window)

window.mainloop()
