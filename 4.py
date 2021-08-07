import math

n = int(input('pls enter a number: '))
if n == 1 :
    print('Can\'t create a snake.pls enter a number in range >1')

elif n%2 != 0 and n != 1 :
    
    for i in range(1,math.ceil(n/2)+1):
        print('*',end='')

        if i == math.ceil(n/2):
            break

        for j in range(1):
            print('#',end='')

elif n%2 == 0:
    for i in range(1,int((n/2)+1)):
        print('*',end='')

        for j in range(1):
            print('#',end='')