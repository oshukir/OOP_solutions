class HighScoreTable:
    
    def __init__(self, size):
        self.size = size
        self.__scores = []
        
    @property
    def scores(self):
        result = sorted(self.__scores, reverse=True)[:self.size] if len(self.__scores) >= self.size else sorted(self.__scores, reverse=True)
        return result
    
    def update(self, score):
        self.__scores.append(score)
    
    def reset(self):
        self.__scores = []

highScoreTable = HighScoreTable(3)
print(highScoreTable.scores == []) # evaluates to True
highScoreTable.update(10)
print(highScoreTable.scores == [10])
highScoreTable.update(8)
highScoreTable.update(12)
highScoreTable.update(5)
highScoreTable.update(10)
print(highScoreTable.scores == [12, 10, 10])
highScoreTable.reset()
print(highScoreTable.scores == [])