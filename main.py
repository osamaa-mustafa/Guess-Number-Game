import random

def guess(x):
    random_number=random.randint(1,x)
    for i in range(3):
        guess = int(input(f'Enter guess number between 1 and {x}\n'))
        if(guess==random_number):
            print('Congrats you have won\n')
            break
        elif(guess>random_number):
            print('Sorry! too high\n')
        elif(guess<random_number):
            print('Sorry! Too low\n')



guess(7)

