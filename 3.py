user_list = []
print('Enter numbers to add your list,when you want to stop,Enter \'stop\'')

while True:
    x = input('pls enter a number: ')

    if x == 'stop':
        break

    else:
        user_list.append(int(x))

print('your list is:',user_list)

c = 0
for i in range(len(user_list)-1):

    if user_list[i] > user_list[i+1] :
        print('Your list is not arranged')
        c += 1
        break

if c != 1:
    print('Your list is arranged')