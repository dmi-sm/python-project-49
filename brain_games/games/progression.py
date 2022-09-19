from random import randint

GAME_RULE = 'What number is missing in the progression?'


def get_question_and_answer():
    start_progression = randint(1, 10)
    step_progression = randint(1, 10)
    length_progression = randint(5, 10)
    missing_number_index = randint(0, length_progression - 1)
    progression = list(range(start_progression, start_progression
                             + length_progression * step_progression,
                             step_progression))
    answer = str(progression[missing_number_index])
    progression[missing_number_index] = '..'
    task = ' '.join(map(str, progression))
    return (task, answer)
