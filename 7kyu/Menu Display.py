# class Menu:
#     def __init__(self, menu: list) -> None:
#         self.menu = menu
#         self.index = 0
#         self.length = len(menu)
    
#     def to_the_right(self) -> None:
#         self.index = (self.index + 1) % self.length
        
#     def to_the_left(self) -> None:
#         self.index = (self.index - 1) % self.length
        
#     def display(self) -> str:
#         temp = self.menu.copy()
#         temp[self.index] = [self.menu[self.index]]
#         return str(temp)
    

################Mine solution#########################

class Menu:
    def __init__(self, menu):
        self.menu = menu
        self.index = 0
    
    def to_the_right(self):
        self.index = (self.index + 1) % (len(self.menu))
        
    def to_the_left(self):
        self.index = (self.index - 1) % (len(self.menu))

        if self.index < 0:
            self.index = len(self.menu)
        
    def display(self):
        result = ', '.join([f"['{item}']" if i == self.index else f"'{str(item)}'" 
                            for i, item in enumerate(self.menu)])
        return '['+result+']'