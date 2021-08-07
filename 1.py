import random
words = ['computer','game','movie','series','programming','python','tree','apple','engineer','doctor','witcher']

word = random.choice(words)
#print(word)
char_list = []
picked_letters = []

for i in range(len(word)):
    char_list.append('-')

life = 5
while life > 0 :
    print(' '.join(char_list))
    print()

    if (''.join(char_list)) == word:
        print('Well done,You Win!')
        break
    
    user_char = input('Pls enter a character: ').lower()

    if user_char in picked_letters:
        print('You already guess this letter, try another one')
    
    elif user_char in word:
        
        picked_letters.append(user_char)

        for i in range(len(word)):
            if word[i] == user_char:
                char_list[i] = user_char
    
    else:
        life -= 1
        print(f'Incorrect,You have {life} lives left')
    
    if life == 0 :
        print('Game Over :(')

    