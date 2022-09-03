import prompt
from random import randint
from brain_games.games.welcome_user import welcome_user


def check_even(number):
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return correct_answer


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        i += 1
        number = randint(1, 10)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == check_even(number):
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{check_even(number)}"')
            print(f'Let\'s try again, {name}!')
            break
    if i == 3:
        print(f'Congratulations, {name}!')
