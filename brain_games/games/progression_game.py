import random


DESCRIPTION = 'What number is missing in the progression?'
MIN_LEN_PROGR = 5
MAX_LEN_PROGR = 10
MIN_START_NUM = 1
MAX_START_NUM = 100
MIN_STEP = 1
MAX_STEP = 13


def get_round_data():
    len_progr = random.randint(MIN_LEN_PROGR, MAX_LEN_PROGR)
    start_num_progr = random.randint(MIN_START_NUM, MAX_START_NUM)
    step_progr = random.randint(MIN_STEP, MAX_STEP)

    i = 0
    progr = []
    progr.append(start_num_progr)
    while i < len_progr:
        progr.append(progr[-1] + step_progr)
        i += 1

    index_missing_number = random.randint(0, len_progr - 1)
    missing_number = str(progr[index_missing_number])
    progr[index_missing_number] = '..'
    return ' '.join(map(str, progr)), missing_number
