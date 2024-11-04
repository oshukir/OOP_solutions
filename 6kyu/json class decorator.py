import json

class jsonattr:
    def __init__(self, file_path):
        self.file = file_path

    def __call__(self, cls):

        with open(self.file, 'r') as f:
            data = json.load(f)

        for key, value in data.items():
            setattr(cls, key, value)

        return cls