import math

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.__radius = radius
#         self.__mass = mass
#         self.volume = round(math.pi * 4 / 3 * self.__radius**3, 5)
        
#     def get_radius(self):
#         return self.__radius
    
#     def get_mass(self):
#         return self.__mass
    
#     def get_volume(self):
#         return self.volume
    
#     def get_surface_area(self):
#         return round(math.pi * 4 * self.__radius**2, 5)
    
#     def get_density(self):
#         return round(self.__mass / self.volume, 5)
    
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = round(math.pi * 4 / 3 * self.__radius**3, 5)
        self.surface_area = round(math.pi * 4 * self.__radius**2, 5)
        self.density = round(self.mass / self.volume, 5)

    def __getattr__(self, name):
        return lambda: getattr(self, name[4:])

