from random import randint, choice

START_INFO = 'What number is missing in the progression?'
ROUND_NUMBER = 3

def set_question_answer():
    num1 = randint(1, 10)
    num2 = randint(40, 80)
    progression_length = randint(5, 10)
    step_value = randint(1, 10)
    progression = []
    count = 1

    for i in range(num1, num2, step_value):
        if count <= progression_length:
            progression.append(str(i))
            count +=1
    
    right_answer = choice(progression)
    index_random_num = progression.index(right_answer)
    progression[index_random_num] = '..'
    question = ' '.join(progression)

    return question, right_answer

set_question_answer()