from brain_games.cli import welcome_user
import prompt


def one_round(questions_lst, correct_ans_lst, name):

    print(f'Question: {questions_lst[0]}')
    ans = prompt.string('Answer: ')
    error = 0

    if ans != correct_ans_lst[0]:
        print(f"'{ans}' is wrong answer ;(. \
Correct answer was '{correct_ans_lst[0]}'.")
        print(f"Let's try again, {name}!")
        error += 1
    elif ans == correct_ans_lst[0] and len(correct_ans_lst) > 1:
        print('Correct!')
    else:
        print('Correct!')
        print('Congratilations, {name}!')

    return error


def eng(task, questions_lst, correct_ans_lst):

    name = welcome_user()
    print(task)

    for i in range(3):
        error = one_round(questions_lst, correct_ans_lst, name)
        if error > 0:
            break
        else:
            questions_lst.pop(0)
            correct_ans_lst.pop(0)
