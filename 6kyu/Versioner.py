class VersionExceptionError(Exception): pass

class VersionManager():
    def __init__(self, path: str = '0.0.1'):
        try:
            self.history = [(0,0,1) if path=="" else tuple(map(int, f"{path}.0.0".split('.')[:3]))]
        except ValueError:
            raise VersionExceptionError("Error occured while parsing version!")
        
    def major(self):
        major, _, _ = self.history[-1]
        self.history.append((major + 1, 0, 0))
        return self
    
    def minor(self):
        major, minor, _ = self.history[-1]
        self.history.append((major, minor+1, 0))
        return self
    
    def patch(self):
        major, minor, patch = self.history[-1]
        self.history.append((major, minor, patch+1))
        return self

    def release(self):
        return "{}.{}.{}".format(*self.history[-1])
    
    def rollback(self):
        if len(self.history) <= 1: raise VersionExceptionError('Cannot rollback!') 
        self.history.pop()
        return self




VersionManager().patch().release()
















































# class VersionManagerException(Exception): pass

# class VersionManager:
#     def __init__(self, version: str = '0.0.1') -> None:
#         try:
#             self.history = [(0,0,1) if version == '' else tuple(map(int, f'{version}.0.0'.split('.')[:3]))]
#         except ValueError:
#             raise VersionManagerException('Error occured while parsing version!')
    
#     def release(self) -> str:
#         return '{}.{}.{}'.format(*self.history[-1])
    
#     def major(self) -> 'VersionManager':
#         major, _, _ = self.history[-1]
#         self.history.append((major + 1, 0, 0))
#         return self
    
#     def minor(self) -> 'VersionManager':
#         major, minor, _ = self.history[-1]
#         self.history.append((major, minor + 1, 0))

#     def patch(self) -> 'VersionManager':
#         major, minor, patch = self.history[-1]
#         self.history.append((major, minor, patch + 1))
#         return self
    
#     def rollback(self) -> 'VersionManager':
#         if len(self.history) <= 1: raise VersionManagerException('Cannot rollback!')
#         self.history.pop()
#         return self