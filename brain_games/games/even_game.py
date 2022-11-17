import random

START_INFO = 'Answer "yes" if the number is even, otherwise answer "no".'
ROUND_NUMBER = 3


def is_even(number):
    return "yes" if (number % 2 == 0) else "no"


def set_question_answer():
    number = random.randint(1, 100)
    right_answer = is_even(number)
    return number, right_answer
