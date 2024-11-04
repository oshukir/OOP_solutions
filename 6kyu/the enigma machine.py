class PlugBoardException(Exception):
    pass

class Plugboard(object):
    def __init__(self, wires = ""):
        if self.is_valid(wires):
            self.wires_dict = self.dict_maker(wires)

    def is_valid(self, plugboard):
        if len(plugboard) > 20:
            raise PlugBoardException("Too many wires defined")
        
        if len(set(plugboard)) != len(plugboard):
            raise PlugBoardException("Duplicate characters are not allowed in wires")
        
        if len(plugboard) % 2 != 0:
            raise PlugBoardException("Wires should be in pairs")

        return True

    def dict_maker(self, wires):
        new_dict = {}

        for i in range(0, len(wires), 2):
            new_dict[wires[i]] = wires[i+1]
            new_dict[wires[i+1]] = wires[i]

        return new_dict

    def process(self, c):
        return self.wires_dict.get(c,c)    
    