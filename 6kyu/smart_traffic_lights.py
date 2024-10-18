# class SmartTrafficLight:
#     def __init__(self, st1, st2):
#         self.road_1 = st1[0]
#         self.road_2 = st2[0]
#         self.name_1 = st1[1]
#         self.name_2 = st2[1]
        
#     def turngreen(self):
#         if self.road_1 < self.road_2:
#             self.road_2 = 0
#             return self.name_2
#         elif self.road_1 > self.road_2:
#             self.road_1 = 0
#             return self.name_1
#         else:
#             return None
        
class SmartTrafficLight:
    def __init__(self, a, b):
        self.a = [] if a[0] == b[0] else sorted((a,b))

    def turngreen(self):
        if self.a:
            return self.a.pop()[1]
        
t = SmartTrafficLight([45, '27th ave'], [73, '3rd st'])
print(t.turngreen())
print(t.turngreen())
print(t.turngreen())