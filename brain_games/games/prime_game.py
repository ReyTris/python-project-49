import random

START_INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ROUND_NUMBER = 3

def is_prime(number):
    if number < 2: return False

    for x in range(2, number - 1):
        if (number % x == 0):
            return False
    else:
        return True


def set_question_answer():
    question = random.randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer