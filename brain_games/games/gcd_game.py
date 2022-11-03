import random


START_NUMBER = 1
END_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    number_1 = random.randint(START_NUMBER, END_NUMBER)
    number_2 = random.randint(START_NUMBER, END_NUMBER)
    question = f'{number_1} {number_2}'
    correct_answer = str(find_gcd(number_1, number_2))
    return question, correct_answer


def find_gcd(num1, num2):
    common_divisors = []
    for i in range(1, min(num1 + 1, num2 + 1)):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)

    return max(common_divisors)
