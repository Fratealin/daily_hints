#! /usr/local/bin/python3

# show user a python or linux tip for each day reading from lists in different files
# use subprocess. Popen to open a sound file (only works on osX)
# plays an ambient noise just for fun
# remove items from list using list.remove(' '), list.pop(n) and append to end
# shelve to remember which file has to be opened next
# use path to create a path object and glob to find all files ending in .mp3
# use of lambda anonymous function to reduce repetition

from tkinter import Tk
import hint_manager
import sound_manager
import random_color_generator


class dailyHintUi:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(expand=YES, fill=BOTH)

        todays_reminder = hint_manager.get_next_topic()
        self.label = Label(frame, text=todays_reminder, height=10, width=90, bg="black", fg=random_color_generator.get_random_color(),
                           font="Arial 40")
        self.label.pack(expand=YES, fill=BOTH)

        self.Button_j = Button(frame, text="japanese hint", bg='blue', font="Arial 25", command=lambda: self.command_display_next_hint("./dailyjapan.txt"))
        self.Button_j.pack(expand=YES, fill=BOTH)

        self.Button_c = Button(frame, text="chinese hint", bg='blue', font="Arial 25", command=lambda: self.command_display_next_hint("./dailychinese.txt"))
        self.Button_c.pack(expand=YES, fill=BOTH)

        self.Button_p = Button(frame, text="python hint", bg='blue', font="Arial 25", command=lambda: self.command_display_next_hint("./dailypython.txt"))
        self.Button_p.pack(expand=YES, fill=BOTH)

        self.Button_l = Button(frame, text="linux hint", bg='blue', font="Arial 25", command=lambda: self.command_display_next_hint("./dailypython.txt"))
        self.Button_l.pack(expand=YES, fill=BOTH)

        self.Button_r = Button(frame, text="romanian hint", bg='blue', font="Arial 25", command=lambda: self.command_display_next_hint("./dailyrom.txt"))
        self.Button_r.pack(expand=YES, fill=BOTH)

        # the function doesn't have a (), because you're not calling it. just assigning it.
        self.nextButton = Button(frame, text="next topic", bg='blue', font="Arial 25", command=self.command_display_next_topic)
        self.nextButton.pack(side=TOP, fill=X)

        # built in quit function
        self.quitButton = Button(frame, text="finish and close", bg='blue', font="Arial 25", command=frame.quit)
        self.quitButton.pack(side=TOP, fill=X)

    def display_finish_button(self):
        self.quitButton.pack(side=TOP, fill=X)

    def command_display_next_hint(self, data_file_path):
        sound_manager.play_sound()
        todays_reminder = hint_manager.get_next_hint(data_file_path)
        self.label.config(fg=random_color_generator.get_random_color(), text=todays_reminder)

    def command_display_next_topic(self):
        sound_manager.play_sound()
        todays_reminder = hint_manager.get_next_topic()
        self.label.config(fg=random_color_generator.get_random_color(), text=todays_reminder)


sound_manager.play_sound()
guiToolKit = Tk()
guiToolKit.title("daily hint - 每日提醒 - momento zilnic")
reminderUi = dailyHintUi(guiToolKit)

guiToolKit.mainloop()
