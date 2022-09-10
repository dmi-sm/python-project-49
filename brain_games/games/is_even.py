from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no"'


def is_even(task):
    return 'yes' if task % 2 == 0 else 'no'


def game():
    task = randint(1, 10)
    answer = is_even(task)
    return (task, answer)
