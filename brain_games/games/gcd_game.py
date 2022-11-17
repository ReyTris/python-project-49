import random, math

START_INFO = 'Find the greatest common divisor of given numbers.'
ROUND_NUMBER = 3


def set_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    right_answer = str(math.gcd(num1, num2))

    return question, right_answer