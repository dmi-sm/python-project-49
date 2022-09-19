from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_question_and_answer():
    task = randint(1, 10)
    answer = 'yes' if task % 2 == 0 else 'no'
    return (task, answer)
