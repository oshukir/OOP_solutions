from re import search as re_search

class WordDictionary:
    def __init__(self):
        self.wd = {}

    def add_word(self, word):
        
        if not len(word) in self.wd:
            self.wd[len(word)] = [word]
        else:
            self.wd[len(word)].append(word)

    def search(self, pattern):
        size = len(pattern)
        
        if not size in self.wd:
            return False
        
        
        for i in self.wd[size]:
            matches = re_search(pattern, i)
            
            if matches != None:
                return True
            
        return False
    
wd = WordDictionary()
wd.add_word("a")
wd.add_word("at")
wd.add_word("ate")
wd.add_word("ear")
wd.search("a")
wd.search("a.")