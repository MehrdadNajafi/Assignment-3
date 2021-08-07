import random

n = int(input('pls enter the number of list: '))
rand_list = []
rand_list = random.sample((range(0,n+10)),n)

print(rand_list)

"""

n = int(input('pls enter the number of list: '))
rand_list = []

while n != len(rand_list):
    item = random.randint(0,n*n)
    
    if item not in rand_list:
        rand_list.append(item)

print(rand_list)

"""