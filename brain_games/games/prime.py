def prime_logic():
    import random
    from brain_games.engine import eng

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        num = random.randint(1, 100)
        questions_lst.append(num)

        if num > 1:
            for j in range(1, num):
                if j > 1 and num % j == 0:
                    correct_ans = 'no'
                    break
                else:
                    correct_ans = 'yes'
        else:
            correct_ans = 'no'

        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
