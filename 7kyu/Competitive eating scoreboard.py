class Person:
    def __init__(self, person: dict):
        self.name = person.get('name')
        self.chickenwings = person.get('chickenwings',0)
        self.hamburgers = person.get('hamburgers',0)
        self.hotdogs = person.get('hotdogs',0)

    def get_score(self):
        return self.chickenwings * 5 + self.hamburgers * 3 + self.hotdogs * 2
    
def sort_key(k):
    return (-k['score'], k['name'])

def scoreboard(who_ate_what):
    scores = []
    for person in who_ate_what:
        p = Person(person)
        scores.append({"name": p.name, "score": p.get_score()})
    return sorted(scores, key=sort_key)
    