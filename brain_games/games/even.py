def even_logic():
    import random
    from brain_games.engine import eng

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        num = random.randint(0, 100)
        questions_lst.append(num)

        if num % 2 != 0:
            correct_ans = 'no'
        else:
            correct_ans = 'yes'

        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
