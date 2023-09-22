from random import randint, choice


MIN_VALUE, MAX_VALUE = 0, 100
ROUNDS = 3
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

    correct_answer = get_correct_answer(random_operator, num1, num2)

    return correct_answer, num1, num2, random_operator


def get_questions_and_answers():

    questions_list = []
    correct_answers_list = []

    for i in range(ROUNDS):
        correct_answer, num1, num2, operator = generate_calc()
        questions_list.append(f'{num1} {operator} {num2}')
        correct_answers_list.append(str(correct_answer))

    return questions_list, correct_answers_list
