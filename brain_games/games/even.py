from random import randint


MIN_VALUE, MAX_VALUE = 0, 100
ROUNDS = 3
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_even():

    num = randint(MIN_VALUE, MAX_VALUE)

    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, num


def get_questions_and_answers():

    questions_list = []
    correct_answers_list = []

    for i in range(ROUNDS):
        correct_answer, num = generate_even()
        questions_list.append(num)
        correct_answers_list.append(correct_answer)

    return questions_list, correct_answers_list
