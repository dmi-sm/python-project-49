from random import randint
from brain_games.games.welcome_user import welcome_user
from brain_games.games.game_engine import game
from brain_games.games.Сonstant import WINSCORE


def right_answer(result):
    for i in range(2, (result // 2) + 1):
        if result % i == 0:
            return 'no'
    return 'yes'


def is_prime():
    user_score = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while user_score < WINSCORE + 1:
        result = randint(2, 10)
        if game(result, right_answer(result), name, user_score):
            user_score += 1
        else:
            break
