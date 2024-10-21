#Something goes Here ...

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    #The rest goes here
    def __add__(self, other):
        bottom = self.bottom*other.bottom
        topper = (bottom / self.bottom) * self.top + (bottom / other.bottom) * other.top
        common_divisor = self.__gcd(topper, bottom)
        return Fraction(topper // common_divisor, bottom // common_divisor)
    
    def __str__(self):
        return f"{int(self.top)}/{int(self.bottom)}"
    
    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a