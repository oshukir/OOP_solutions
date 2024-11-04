class Converter():
    @staticmethod
    def to_ascii(h):
        ascii_string = ''.join(chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2))
        return ascii_string
    
    @staticmethod
    def to_hex(s):
        hex_values = [format(ord(char), '02x') for char in s]
        return "".join(hex_values)