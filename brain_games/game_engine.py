import prompt

WINSCORE = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def run_game(game):
    user_score = 0
    name = welcome_user()
    print(game.GAME_RULE)
    while user_score < WINSCORE:
        task, answer = game.game()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            user_score += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f' Correct answer was "{answer}".'
                  f'\nLet\'s try again, {name}!')
            break
    if user_score == WINSCORE:
        print(f'Congratulations, {name}!')
        return
