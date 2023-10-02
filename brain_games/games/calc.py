from random import randint, choice


MIN_VALUE, MAX_VALUE = 0, 100
OPERATORS = ('+', '-', '*')
TASK = 'What is the result of the expression?'


def get_correct_answer(random_operator, num1, num2):

    if random_operator == '+':
        correct_answer = num1 + num2
    elif random_operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return correct_answer


def generate_calc():

    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    random_operator = choice(OPERATORS)

    question = f'{num1} {random_operator} {num2}'
    correct_answer = str(get_correct_answer(random_operator, num1, num2))

    return question, correct_answer
