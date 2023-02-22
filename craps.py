from random import randint


def newCraps(sum):
    print(f'Now your goal number is {sum}')
    isWin = True
    while isWin:
        newD1, newD2 = randint(1, 6), randint(1, 6)
        gumar = newD1 + newD2
        text = f'The sum of dice is {newD1} + {newD2} = {gumar}'
        print(text)
        if gumar == sum:
            print('You won')
            isWin = False
        elif gumar == 7:
            print('You lose')
            isWin = False


def craps():
    dice1, dice2 = randint(1,6), randint(1,6)
    gumar = dice1 + dice2
    isWin = [7, 11]
    isLose = [2, 3, 12]
    text = f'The sum of dice is {dice1} + {dice2} = {gumar}'
    print(text)

    if gumar in isWin:
        print('You won')
    elif gumar in isLose:
        print('Casino won')
    else:
        newCraps(gumar)

craps()

