#! /usr/local/bin/python3

import shelve, sys, os, subprocess, shelve

# show user a python or linux tip for each day reading from lists in different files
# learnt to: open a file with default program using os.popen
# remove items from list using list.remove(' '), list.pop(n) and append to end


'''
shelfFile = shelve.open('daily_order')
file_names = []
shelfFile['file_names'] = file_names
shelfFile.close()

shelfFile = shelve.open('daily_order')
file_names = ["./dailylinux.txt", "./dailypython.txt", "./dailychinese.txt", "./dailyjapan.txt", "./dailyrom.txt"]
shelfFile['file_names'] = file_names
shelfFile.close()
'''




import logging
logging.basicConfig(level=logging.DEBUG)

#Put this line where you want to see if there's an error
logging.debug('The Log message.')
# eg., logging.debug(type(first))

# put this line in to disable logging messages
logging.disable(logging.CRITICAL)



def get_todays_python():
    with open("dailypython.txt") as fileObject:
        links = fileObject.read()
        paragraphs = links.split("\n\n")
        fileObject.close()
        for para in paragraphs:

            pythondata = para.split('\n')
            #remove blank items in list
            while '' in pythondata:
                pythondata.remove('')
            removed_item = pythondata.pop(0)
            pythondata.append(removed_item)

            with open("./dailypython.txt", "w") as fileObject:
                fileObject.write("\n\n".join(pythondata))
                fileObject.close()


            return removed_item




def get_todays_data(file_name):
    with open(file_name) as fileObject:
        data = fileObject.read()
        paragraphs = data.split("\n\n")
        fileObject.close()

        #paragraphs = para.split('\n\n')
        #remove blank items in list
        '''
        while '' in paragraphs:
            paragraphs.remove('')
        '''
        #read first item to display to user. Remove with pop, and append to end.
        removed_item = paragraphs.pop(0)
        paragraphs.append(removed_item)

        with open(file_name, "w") as fileObject:
            fileObject.write("\n\n".join(paragraphs))
            fileObject.close()
        return removed_item



def display_all():
    linux_file = "./dailylinux.txt"
    python_file = "./dailypython.txt"
    chinese_file = "./dailychinese.txt"
    japan_file = "./dailyjapan.txt"
    rom_file = "./dailyrom.txt"
    with open('todays_reminder.txt', 'w') as fileObject:
        fileObject.write("--Todays Python--\n\n%s" % (get_todays_data(python_file)) + "\n\n\n--Todays Linux--\n\n%s" % (get_todays_data(linux_file)) + "\n\n\n--Todays Japanese--\n\n%s" % (get_todays_data(japan_file)) + "\n\n\n--Todays Chinese--\n\n%s" % (get_todays_data(chinese_file)) + "\n\n\n--Todays Romanian--\n\n%s" % (get_todays_data(rom_file)))
        fileObject.close()
    subprocess.Popen(['open', 'todays_reminder.txt'])

#display_all()

def display_one():

    # find which file needs to be opened next
    shelfFile = shelve.open('daily_order')
    file_names = shelfFile['file_names']

    #remove / pop first item and move to end
    next_file = file_names.pop(0)
    file_names.append(next_file)
    #update shelf file
    shelfFile['file_names'] = file_names
    shelfFile.close()

    with open('todays_reminder.txt', 'w') as fileObject:
        fileObject.write("--Todays Reminder--\n\n%s" % (get_todays_data(next_file)))
        fileObject.close()
    subprocess.Popen(['open', 'todays_reminder.txt'])







display_one()