from preloaded import TEXT2HEX

class HexCipher:

    HEX2TEXT = {h: c for c,h in TEXT2HEX.items()}

    @classmethod
    def encode(cls, s, n):
        for _ in range(n): s = ''.join([TEXT2HEX[i] for i in s])
        return s
    
    @classmethod
    def decode(cls, s, n):
        for _ in range(n): s = "".join([HexCipher.HEX2TEXT[s[i:i+2]] for i in range(0, len(s), 2)])
        return s
    