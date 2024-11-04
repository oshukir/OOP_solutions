class Harshad:
    @staticmethod
    def is_valid(number):
        if number % Harshad.sum_of_digits(number) == 0:
            return True
        
        return False
    
    @staticmethod
    def get_next(number):
        number += 1
        while True:
            if Harshad.is_valid(number):
                return number
            
            number += 1
    
    @staticmethod
    def get_series(count, start=0):
        result = []
        for i in range(count):
            start = Harshad.get_next(start)
            
            result.append(start)
            
        return result
        
    @staticmethod
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))