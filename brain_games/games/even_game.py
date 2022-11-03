
import random


START_NUMBER = 1
END_NUMBER = 300
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_data():
    random_number = random.randint(START_NUMBER, END_NUMBER)

    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = random_number
    return question, correct_answer


def is_even(random_number):
    return random_number % 2 == 0
