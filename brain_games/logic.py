import prompt


SCORE = 3


def lounch(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    index = 0
    while index < SCORE:
        question, correct_answer = game.get_round_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {name}!")
            return
        index += 1

    print(f'Congratulations, {name}!')
