class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = list(map1)
        self.map2 = list(map2)
        
        self.encoding_dict = dict(zip(map1, map2))
        self.decoding_dict = dict(zip(map2, map1))
    
    def encode(self, s):
        
        encoded = "".join(self.encoding_dict.get(i, i) for i in s)
        return encoded
    
    def decode(self, s):
        
        decoded = "".join(self.decoding_dict.get(i, i) for i in s)
        return decoded
