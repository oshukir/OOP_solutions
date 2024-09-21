import string

class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if new_name.isalnum() and new_name[0] in string.ascii_uppercase:
            cls.__name__ = new_name
        else:
            raise NameError("Name a class with upper-case letter")
        
    @classmethod
    def __str__(cls):
        return (f"Class name is: {cls.__name__}")