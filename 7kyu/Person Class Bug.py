# class Person():

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = self.first_name + " " + self.last_name

class Person():

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @property
    def full_name(self):
        return self.__first_name + " " + self.__last_name