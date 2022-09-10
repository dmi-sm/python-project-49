from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(task):
    for i in range(2, (task // 2) + 1):
        if task % i == 0:
            return 'no'
    return 'yes'


def game():
    task = randint(2, 10)
    answer = is_prime(task)
    return (task, answer)
