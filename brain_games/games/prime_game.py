import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_round_data():
    question_number = random.randint(1, 301)
    if is_prime(question_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_number, correct_answer


def is_prime(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        return True
    else:
        return False
