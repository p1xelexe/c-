from random import choice
from second import get_word, table, get_lives
lives = get_lives
#lives = (5, 4, 3, 2, 1)
max_wrong = len(lives)
#WORDS = ('python', 'p1xel')
#word = choice(WORDS)
word = get_word
so_far = table
#so_far = '_' * len(word)
wrong = 0
used = []
while wrong < lives and so_far != word:
    print(lives[wrong])
    print('\nВы использовали следующие буквы\n', used)
    print('\nУгадай\n', so_far)
    guess = input('\n Введи букву: ')
    while guess in used:
        print('вы уже угадали букву', guess)
        guess = input('\n Введи букву: ')
    used.append(guess)
    if guess in word:
        print('\n ДА!', guess)
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
