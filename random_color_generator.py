import random

def get_random_color():
    colors = "red blue green purple gray brown navy orange orchid4"
    color_list = colors.split()
    return random.choice(color_list)