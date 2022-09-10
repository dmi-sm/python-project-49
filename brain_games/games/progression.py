from random import randint

GAME_RULE = 'What number is missing in the progression?'


def progression(start_progression, step_progression, length_progression):
    return [str(i) for i in range(start_progression,
            start_progression + length_progression * step_progression,
            step_progression)]


def game():
    start_progression = randint(1, 10)
    step_progression = randint(1, 10)
    length_progression = 5
    missing_number_index = randint(0, length_progression - 1)
    task = progression(start_progression, step_progression, length_progression)
    answer = task[missing_number_index]
    task[missing_number_index] = '..'
    task = ' '.join(task)
    return (task, answer)
