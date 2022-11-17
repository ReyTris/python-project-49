from brain_games import cli


def engine(script_game):
    name = cli.welcome_user(script_game.START_INFO)

    for x in range(script_game.ROUND_NUMBER):
        question, right_answer = script_game.set_question_answer()

        answer = cli.get_answer(question)

        if int(answer) != int(right_answer):
            cli.wrong_answer(right_answer, answer, name)
            break
        cli.right_answer()
    else:
        cli.win_game(name)
