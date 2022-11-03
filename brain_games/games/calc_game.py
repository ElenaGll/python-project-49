import random


START_NUMBER = 1
END_NUMBER = 50
DESCRIPTION = 'What is the result of the expression?'


def get_round_data():
    number_1 = random.randint(START_NUMBER, END_NUMBER)
    number_2 = random.randint(START_NUMBER, END_NUMBER)
    oper = random.choice(('+', '-', '*'))

    question = str(number_1) + ' ' + oper + ' ' + str(number_2)
    correct_answer = str(calculate(number_1, number_2, oper))
    return question, correct_answer


def calculate(number_1, number_2, oper):
    if oper == '+':
        return number_1 + number_2
    elif oper == '-':
        return number_1 - number_2
    elif oper == '*':
        return number_1 * number_2
