class UnexpectedTypeException(Exception):
    def __init__(self, types):
        self.types = types
    
    def __str__(self):
        return f"Was expecting instance of: {', '.join(self.types)}"

class expected_type:
    
    def __init__(self, types):
        self.__types = types
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            
            result = func(*args, **kwargs)
            
            if not type(result) in self.__types:
                raise UnexpectedTypeException(self.__types)
            
            return result
        
        return wrapper
        
@expected_type((str,))
def return_something(something):
    return something

lol = return_something('loool')