from random import randint


MIN_VALUE, MAX_VALUE = 1, 10
MIN_DIFFERENCE, MAX_DIFFERENCE = 1, 20
HIDDEN_INDEX_MIN, HIDDEN_INDEX_MAX = 0, 9
PROGRESSION_LENGTH = 10
ROUNDS = 3
TASK = 'What number is missing in the progression?'


def get_progression(num, difference):

    progression = []
    progression.append(num)

    for i in range(PROGRESSION_LENGTH - 1):
        next_num = num + difference
        progression.append(next_num)
        num = next_num

    return progression


def generate_progression():

    num = randint(MIN_VALUE, MAX_VALUE)
    difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)

    progression = get_progression(num, difference)

    hidden_index = randint(HIDDEN_INDEX_MIN, HIDDEN_INDEX_MAX)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    return correct_answer, progression


def get_questions_and_answers():

    questions_list = []
    correct_answers_list = []

    for i in range(ROUNDS):
        correct_answer, progression = generate_progression()
        correct_answers_list.append(correct_answer)
        questions_list.append(' '.join(map(str, progression)))

    return questions_list, correct_answers_list
