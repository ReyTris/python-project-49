import prompt, random


def test_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        num = random.randrange(100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if (num % 2 == 0 and answer == 'yes') or (num % 2 != 0 and answer == 'no'):
            print('Correct!')
            num = random.randrange(100)
            count += 1
        elif (num % 2 == 0 and answer != 'yes'):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
    else:
        print('Congratulations, Bill!')
    
def main():
    test_even()


if __name__ == '__main__':
    main()