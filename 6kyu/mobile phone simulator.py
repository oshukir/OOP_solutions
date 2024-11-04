class Phone:
    def __init__(self):
        self.screen = ""
        self.microphone = ""
        self.ring = ""
        self.contacts = [
            {'name': "John", 'number': 11111111, 'ring': "Do Re Mi"},
            {'name': "Doe", 'number': 22222222, 'ring': "Mi Re Do"},
            {'name': "Jack", 'number': 33333333, 'ring': "Fa So La Ti"}
        ]
        self.current_call = None
    
    def incomingcall(self, number):
        contact = next((contact for contact in self.contacts if contact['number'] == number), None)
        
        if contact:
            self.screen = f"Call: {contact['name']}\nNumber: {contact['number']}"
            self.ring = contact['ring']
            self.current_call = contact['name']
        else:
            self.screen = f"Call: stranger\nNumber: {number}"
            self.ring = "Di Da Di"
            self.current_call = "stranger"
    
    def connect(self):
        self.ring = ""
        self.screen = ""
        if self.current_call == "stranger":
            self.microphone = "Hello, who is speaking, please?"
        else:
            self.microphone = f"Hello, {self.current_call}!"
    
    def hangup(self):
        self.ring = ""
        self.screen = ""
        self.microphone = ""
        self.current_call = None