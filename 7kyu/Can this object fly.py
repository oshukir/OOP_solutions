class Journey:
    
    def __init__(self, object, crew, balloons):
        self.base_weight = object['weight']
        self.crew_weight = crew * 80 
        self.balloons_lifts = balloons * 0.0048
    
    
    def isPossible(self):
        return self.balloons_lifts >= self.base_weight + self.crew_weight