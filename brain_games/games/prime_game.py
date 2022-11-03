import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'
START_NUMBER = 1
END_NUMBER = 301


def get_round_data():
    question_number = random.randint(START_NUMBER, END_NUMBER)

    if is_prime(question_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
        
    return question_number, correct_answer


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, random_number):
        if num % i == 0:
            return False

    return True
