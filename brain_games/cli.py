import prompt


def welcome_user(start_info):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{start_info}')
    return name


def get_answer(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def wrong_answer(right_answer, your_answer, name):
    print(f"""'{your_answer}' is wrong answer ;(.
        Correct answer was '{right_answer}'. Let's try again, {name}!""")


def right_answer():
    print('Correct!')


def win_game(name):
    print(f'Congratulations, {name}!')
