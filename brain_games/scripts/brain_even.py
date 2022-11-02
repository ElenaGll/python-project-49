# !/usr/bin/env python3


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    even_game(name)


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i < 4:
        random_number = random.randint(1, 100)
        rem = random_number % 2
        print(f'Quwstion: {random_number}')
        answer = prompt.string('Your answer: ')
        if (rem == 0 and answer == 'yes') or (rem == 1 and answer == 'no'):
            print('correct!')
        else:
            if rem == 0 and (answer == 'no' or answer not in ('yes', 'no')):
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'."
                      f"\nLet's try again, {name}!")
                break
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'."
                      f"\nLet's try again, {name}!")
                break
        i += 1
    if i == 4:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
