# class Automaton(object):

#     def __init__(self):
#         self.cr_state = 0

#     def read_commands(self, commands):
#         for i in commands:
#             if self.cr_state == 0:
#                 if i == "1":
#                     self.cr_state += 1
            
#             elif self.cr_state == 1:
#                 if i == "0":
#                     self.cr_state += 1
                    
#             elif self.cr_state == 2:
#                 self.cr_state -= 1
        
#         return self.cr_state == 1

# my_automaton = Automaton()

# print(my_automaton.read_commands(["1", "0", "1", "0", "0"]))





#############################2#################################
# class Automaton(object):

#     def __init__(self):
#         self.automata = {
#             ('q1', '1'): 'q2', ('q1', '0'): 'q1',
#             ('q2', '1'): 'q2', ('q2', '0'): 'q3',
#             ('q3', '1'): 'q2', ('q3', '0'): 'q2',
#         }

#         self.state = 'q1'

#     def read_commands(self, commands):
#         for c in commands:
#             self.state = self.automata[(self.state, c)]

#         return self.state == 'q2'
    
# my_automaton = Automaton()


#############################3################################

class Automaton(object):

    states = [[0,1], [2,1], [1,1]]

    def read_commands(self, commands):
        s = 0
        for i in commands:
            s = self.states[s][int(i)]
        return s == 1
    
my_automaton = Automaton()