from random import sample, choice
from string import ascii_letters

def generateName(length=6):
    while True:
        name = ''.join(sample(ascii_letters, length))
        if not photoManager.nameExists(name):
            return name
        

        