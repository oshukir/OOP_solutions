class Guesser:
    def __init__(self, number, lives):
        self._number = number
        self._lives = lives
        
    def __check(self, n):
        return self._number == n
  
    def guess(self, n):
        if self._lives < 1:
            raise "Too many guesses"
        elif self.__check(n):
            return True
        else:
            self._lives -= 1
            return False