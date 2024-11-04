from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class list:
    content: List[Any] = field(default_factory=list)
    
    def even(self):
        return [element for element in self.content if isinstance(element, int) and element % 2 == 0]
    
    def odd(self):
        return [element for element in self.content if isinstance(element, int) and element % 2 == 1]
    
    def under(self, upperbound):
        return [element for element in self.content if isinstance(element, int) and element < upperbound]
    
    def over(self, lowerbound):
        return [element for element in self.content if isinstance(element, int) and element > lowerbound]
    
    def in_range(self, lowerbound, upperbound):
        return [element for element in self.content if isinstance(element, int) and element >= lowerbound and element <= upperbound]