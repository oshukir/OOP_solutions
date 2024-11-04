import time

class timer:
    def __init__(self, amount):
        self.amount = amount

    def __call__(self, foo):
        def wrapper(*args, **kwargs):
            start = time.time()

            foo(*args, **kwargs)

            end = time.time()

            return (end - start) < self.amount
        
        return wrapper
    

# import time

# def timer(amount):
#     def inner(foo):
#         def wrapper(*args, **kwargs):
#             start = time.time()  # Start the timer

#             result = foo(*args, **kwargs)  # Call the wrapped function with its original arguments

#             end = time.time()  # End the timer

#             return (end - start) < amount# Return if it meets the time requirement and foo's result
        
#         return wrapper
#     return inner