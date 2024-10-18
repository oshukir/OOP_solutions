class Router(object):
    
    def __init__(self):
        self.action = {}
    
    def bind(self, url, http, action):
        if url not in self.action:
            self.action[url] = {}
        self.action[url][http] = action
    
    def runRequest(self, url, http):
        if url in self.action and http in self.action[url]:
            return self.action[url][http]()
        else:
            return 'Error 404: Not Found'


router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')

print(router.runRequest('/hello', 'GET'))