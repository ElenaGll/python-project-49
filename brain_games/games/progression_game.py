import random


DESCRIPTION = 'What number is missing in the progression?'


def get_round_data():
    len_progr = random.randint(5, 10)
    start_num_progr = random.randint(1, 100)
    step_progr = random.randint(1, 13)

    i = 0
    progr = []
    progr.append(start_num_progr)
    while i < len_progr:
        progr.append(progr[-1] + step_progr)
        i += 1

    index_missing_number = random.randint(0, len_progr - 1)
    missing_number = str(progr[index_missing_number])
    progr[index_missing_number] = '..'
    return progr, missing_number
