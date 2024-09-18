class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []
        
    def how_many(self, my_list: list):
        new_listeners = set(list(map(lambda x: x.lower(), my_list)))
        new_listeners = list(filter(lambda x: not(x in self.listeners), new_listeners))
        
        self.listeners.extend(new_listeners)
        
        return len(new_listeners)
    
#############################################Second Solution#########################################################
# class Song:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#         self._seen = set()
    
#     def how_many(self, people):
#         tmp = set(map(str.lower, people))
#         res = len(tmp - self._seen)
#         self._seen.update(tmp)
#         return res