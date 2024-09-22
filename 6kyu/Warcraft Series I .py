class Worker():
    def __init__(self, position, direction, base):
        self.position = position
        self.direction = direction
        self.base = base
    
    def move(self):
        if self.position == 0:
            self.direction = 1
        if self.position == self.base:
            self.direction = -1
        self.position += self.direction
        return self.position
        

class Coordinator:
    def __init__(self, path):
        self.workers = []
        self.path_template = ["M"] + ["."] * (len(path) - 2) + ["B"]
        
        self.parse(path)
    
    def parse(self, path):
        for i in range(len(path)):
            if path[i] == "<":
                self.workers.append(Worker(i, -1, len(path) - 1))
            elif path[i] == ">":
                self.workers.append(Worker(i, 1, len(path) - 1))

    def move(self):
        for worker in self.workers:
            worker.move()
    
    def get_path(self):
        path = self.path_template.copy()
        for worker in self.workers:
            match path[worker.position]:
                case ".":
                    path[worker.position] = "<" if worker.direction < 0 else '>'
                case "M":
                    path[worker.position] = "*"
                case "B":
                    path[worker.position] = "*"
                case "<":
                    path[worker.position] = "#"
                case ">":
                    path[worker.position] = "#"
        return "".join(path)
                
            
        

def simulate_mining(path, time):
    result = []
    map = Coordinator(path)
    for i in range(time):
        result.append(map.get_path())
        map.move()
    return result


print("\n".join(simulate_mining('M..<..B', 12)))