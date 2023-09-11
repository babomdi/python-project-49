def prime_logic():

    from brain_games.engine import eng
    from brain_games.check_prime_num import is_prime

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        correct_ans, num = is_prime()
        questions_lst.append(num)
        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
