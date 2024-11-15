#My solution


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

def my_key(item):
    key, value = item
    return -key

def most_money(students: list) -> str:
    new_dict = {}
    
    
    
    for i in students:
        sum = i.fives * 5 + i.tens * 10 + i.twenties * 20
        name = i.name
        
        if new_dict.get(sum, False):
            new_dict[sum].append(name)
        else:
            new_dict[sum] = [name]
            
    if len(new_dict.keys()) == 1 and len(new_dict[new_dict.keys()[0]]) != 1:
        return 'all'
    else:
        sorted_list = sorted(new_dict.items(), key = my_key)
        result =  sorted_list[0][1][0]

        return result
        



#Genious solution


# def most_money(students):
#     total = []
#     for student in students:
#         total.append((student.fives * 5) + (student.tens * 10) + (student.twenties * 20))
    
#     if min(total) == max(total) and len(students) > 1:
#         return "all"
#     else:
#         return students[total.index(max(total))].name