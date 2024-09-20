import string

def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0] in string.ascii_uppercase:
        cls.__name__ = new_name
    else:
        raise "Error"