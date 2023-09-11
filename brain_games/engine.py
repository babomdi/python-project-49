def eng(task, questions_lst, correct_ans_lst):

    from brain_games.cli import welcome_user
    import prompt

    name = welcome_user()

    print(task)
    for i in range(3):
        print(f'Question: {questions_lst[i]}')

        ans = prompt.string('Answer: ')

        if ans != correct_ans_lst[i]:
            print(f"'{ans}' is wrong answer ;(. \
Correct answer was '{correct_ans_lst[i]}'.")
            print(f"Let's try again, {name}!")
            break
        elif ans == correct_ans_lst[i] and i < 2:
            print('Correct!')
        else:
            print('Correct!')
            print(f'Congratulations, {name}!')
