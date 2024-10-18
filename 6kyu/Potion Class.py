from math import ceil
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        new_volume = self.volume + other.volume
        new_color = [ceil(((self.color[i] * self.volume) + (other.color[i] * other.volume)) / new_volume) for i in range(3)]
        
        return Potion(tuple(new_color), new_volume)