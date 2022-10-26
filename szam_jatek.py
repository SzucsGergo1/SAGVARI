import random

def number_guess(x):
    random_number = random.randint(1, x)
    number_guess = 0
    while number_guess != random_number:
        number_guess = int(input(f'Tippelj egy számot 1 és {x} között: '))
        if number_guess < random_number:
            print('Tippelj újra, a szám túl alacsony')
        elif number_guess > random_number:
            print('Tippelj újra, a szám túl magas')

    print(f'Kitaláltad a helyes számot! ({random_number})')

def computer_number_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'h':
        if low != high:
            number_guess = random.randint(low, high)
        else:
            number_guess = low 
        feedback = input(f'{number_guess} szám túl magas (M), túl alacsony (A) vagy helyes (H)?? ').lower()
        if feedback == 'm':
            high = number_guess - 1
        elif feedback == 'a':
            low = number_guess + 1

    print(f'A számítógép kitalálta a számodat! ({number_guess})')


number_guess(3)
