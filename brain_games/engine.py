from brain_games.cli import welcome_user
import prompt


def run_game(task, questions_list, correct_answers_list):

    name = welcome_user()
    print(task)

    ROUNDS = 3
    for i in range(ROUNDS):
        print(f'Question: {questions_list[0]}')
        answer = prompt.string('Answer: ')
        correct_answer = correct_answers_list[0]

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        elif answer == correct_answer and len(correct_answers_list) > 1:
            print('Correct!')
            questions_list.pop(0)
            correct_answers_list.pop(0)
        else:
            print('Correct!')
            print(f'Congratulations, {name}!')
