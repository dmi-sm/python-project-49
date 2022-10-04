from random import randint

GAME_RULE = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(0, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    stop = start + length * step
    missing_number_index = randint(0, length - 1)
    progression = list(range(start, stop, step))
    answer = str(progression[missing_number_index])
    progression[missing_number_index] = '..'
    task = ' '.join(map(str, progression))
    return (task, answer)
