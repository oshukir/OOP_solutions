# import random

# class Ghost(object):
#   def __init__(self):
#     self.color = random.choice(["white", "yellow", "purple", "red"])


import random

class Ghost(object):
    @property
    def color(self):
        color_list = ['white', 'yellow', 'purple', 'red']
        choice = random.choice(color_list)
        return choice