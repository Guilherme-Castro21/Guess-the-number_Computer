from random import randint


def guess(x):
    random_number = randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f'Guess a number between 1 and {x}: ').strip()

        try:
            guess = int(guess)
        except ValueError:
            print('Value error, not a integer')
            continue
        except Exception:
            print('Unknown error')
            continue

        if guess < random_number:
            print('Sorry, try again. Too low.')
        elif guess > random_number:
            print('Sorry, try again. Too high.')
    print(f'Congrats. You have guessed the correct number: {guess}')


guess(10)
