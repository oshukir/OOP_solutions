class BullsAndCows:
            
    def __init__(self, n):
        if self.__validate(n):
            self._secret = str(n)
            self._turn = 8
            self._victory = False 
        
    def __is_able(self):
        return self._turn > 0
    
    def __validate(self, n):
        n = str(n)
        
        if len(n) != 4 or len(set(n)) != 4 or n[0] == '-':
            raise ValueError
        
        return True
    
    def __find_bulls_cows(self, n):
        b = 0
        c = 0
        n = str(n)
        
        for x, y in zip(n, self._secret):
            if x == y:
                b+=1
            elif x in self._secret:
                c+=1
                
        return (b, c)
                
    
    def compare_with(self, n):
        if self._victory:
            return "You already won!"
        
        if not self.__is_able():
            return "Sorry, you're out of turns!"
        elif self.__validate(n):
            bulls, cows = self.__find_bulls_cows(n)
                
            if bulls == 4:
                self._victory = True
                return("You win!")
            else:
                self._turn -= 1
                return f'{bulls} bull{"s" if bulls != 1 else ""} and {cows} cow{"s" if cows != 1 else ""}'
            

########################SOLUTION 2###################################
# class BullsAndCows:
#     def __init__(self, n):        
#         if not self.allowed(n): raise ValueError()
#         self.n, self.turns, self.solved = str(n), 0, False
        
#     def plural(self, n): return 's' if n != 1 else ''        
#     def allowed(self, n): return 1234 <= n <= 9876 and len(set(c for c in str(n))) == 4
    
#     def compare_with(self, n):
#         if self.solved: return 'You already won!'
#         if self.turns >= 8: return 'Sorry, you\'re out of turns!'
#         if self.n == str(n): 
#             self.solved = True
#             return 'You win!'
        
#         if not self.allowed(n): raise ValueError()
#         self.turns += 1
        
#         bulls = sum(a == b for a, b in zip(self.n, str(n)))
#         cows = max(len({e for e in self.n} & {e for e in str(n)}) - bulls, 0)
#         return f'{bulls} bull{self.plural(bulls)} and {cows} cow{self.plural(cows)}'



##############################SOLUTION3#################################
