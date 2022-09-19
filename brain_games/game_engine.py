import prompt

ROUNDS_TOTAL = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def run_game(game):
    name = welcome_user()
    print(game.GAME_RULE)
    for _ in range(ROUNDS_TOTAL):
        task, answer = game.get_question_and_answer()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            return print(f'"{user_answer}" is wrong answer ;(.'
                         f' Correct answer was "{answer}".'
                         f'\nLet\'s try again, {name}!')
        print('Correct!')
    return print(f'Congratulations, {name}!')
