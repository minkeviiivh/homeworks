import random
randomlist = [random.randint(-100, 100) for x in range(10)] 
print(randomlist)
randomlist[3] = random.randint(-100, 100) 
randomlist.pop(6)
print(randomlist)
