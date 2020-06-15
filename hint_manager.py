#! /usr/local/bin/python3

import shelve

# this is how to make a shelf file
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

def get_next_hint(file_name):
    with open(file_name) as fileObjectToRead:
        data = fileObjectToRead.read()
        hints_list = data.split("\n\n")
        fileObjectToRead.close()

        #read first item to display to user. Remove with pop, and append to end.
        next_hint = hints_list.pop(0)
        hints_list.append(next_hint)

        with open(file_name, "w") as fileObjectToWrite:
            fileObjectToWrite.write("\n\n".join(hints_list))
            fileObjectToWrite.close()
        return next_hint


def get_next_topic():
    # find which file needs to be opened next
    shelf_file = shelve.open('daily_order')
    file_names = shelf_file['file_names']

    #remove / pop first item and move to end
    next_file = file_names.pop(0)
    file_names.append(next_file)
    #update shelf file
    shelf_file['file_names'] = file_names
    shelf_file.close()
    return get_next_hint(next_file)
