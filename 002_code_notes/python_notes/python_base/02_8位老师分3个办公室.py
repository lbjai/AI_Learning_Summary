import random

teachers = ['A','B','C','D','E','F','G','H']

rooms = [[],[],[]]

for teacher in teachers:
    # random.randint(0,2) 包含0,1,2
    index = random.randint(0,2)
    rooms[index].append(teacher)
print(rooms)