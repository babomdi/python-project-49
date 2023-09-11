def even_logic():

    from brain_games.engine import eng
    from brain_games.functions import random_even

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        correct_ans, num = random_even()
        questions_lst.append(num)
        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
