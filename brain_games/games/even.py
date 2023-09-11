def even_logic():

    from brain_games.engine import eng
    from brain_games.functions import random_even

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_lst = []
    correct_answ_lst = []

    for i in range(3):
        correct_answ, num = random_even()
        question_lst.append(num)
        correct_answ_lst.append(correct_answ)

    eng(task, question_lst, correct_answ_lst)
