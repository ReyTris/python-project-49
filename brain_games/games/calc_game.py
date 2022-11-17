import random, operator

START_INFO = 'What is the result of the expression?'
ROUND_NUMBER = 3

def is_calculate(char, num1, num2):
    
    if char == '+': 
        return num1 + num2
    elif char == '-': 
        return num1 - num2
    else: 
        return num1 * num2

def set_question_answer():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    char = random.choice(['-','+','*'])
    right_answer = is_calculate(char, num1, num2)
    number = f'{str(num1)} {char} {str(num2)}'
    return number, right_answer