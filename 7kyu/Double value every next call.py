class Class:
    __CALL = 0
    @staticmethod
    def get_number():
        value = pow(2, Class.__CALL)
        Class.__CALL += 1
        
        return value