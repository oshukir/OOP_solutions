class Block:
    def __init__(self, dimension: list):
        self.__width = dimension[0]
        self.__length = dimension[1]
        self.__height = dimension[2]
        
    def get_width(self):
        return self.__width
    
    def get_length(self):
        return self.__length
    
    def get_height(self):
        return self.__height
    
    def get_volume(self):
        return (self.__width * self.__length * self.__height)
    
    def get_surface_area(self):
        return (2*self.__width*self.__length) + (2*self.__width*self.__height) + (2*self.__length*self.__height)
    

########################WITH DESCRIPTORS#############################
# class Edge:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value

# class Block:
#     width = Edge()
#     length = Edge()
#     height = Edge()

#     def __init__(self, dimension: list):
#         self.width = dimension[0]
#         self.length = dimension[1]
#         self.height = dimension[2]
    
#     def get_volume(self):
#         return (self.width * self.length * self.height)
    
#     def get_surface_area(self):
#         return (2*self.width*self.length) + (2*self.width*self.height) + (2*self.length*self.height)
    

# block = Block([2,2,2])
# print(block.width)
# print(block.get_surface_area())

# block.width = 1
# print(block.get_surface_area())