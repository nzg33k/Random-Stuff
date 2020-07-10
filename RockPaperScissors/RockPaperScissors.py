"""Rock, Paper, Scissors"""
import random


def get_options(version='normal'):
    if version == 'normal':
        o_options = {
            'r': {
                'name': "rock",
                'beats': {
                    's': "rock crushes scissors"
                }
            },
            'p': {
                'name': "paper",
                'beats': {
                    'r': "paper covers rock"
                }
            },
            's': {
                'name': "scissors",
                'beats': {
                    'p': "scissors cut paper",
                }
            },
            'prompt': "please enter r for rock, s for scissors, or p for paper: "
        }
    else:
        o_options = {
            'r': {
                'name': "rock",
                'beats': {
                    's': "(and as it always has) Rock crushes Scissors",
                    'l': "rock crushes lizard",
                }
            },
            'p': {
                'name': "paper",
                'beats': {
                    'r': "paper covers rock",
                    'v': "paper disproves spock"
                }
            },
            's': {
                'name': "scissors",
                'beats': {
                    'p': "scissors cut paper",
                    'l': "scissors decapitate lizard"
                }
            },
            'l': {
                'name': "lizard",
                'beats': {
                    'p': "lizard eats paper",
                    'v': "lizard poisons Spock"
                }
            },
            'v': {
                'name': "spock",
                'beats': {
                    's': "Spock smashes scissors",
                    'r': "Spock vapourises rock"
                }
            },
            'prompt': "please enter r for rock, s for scissors, p for paper, l for lizard, or v for (Vulcan) Spock: "
        }
    return o_options


def who_won_round(player_one_choice, player_two_choice, wwr_options, print_reason=True):
    """Figure out who won"""
    if player_one_choice == player_two_choice:
        winner = 'no one'
        reason = "You both picked " + wwr_options[player_one_choice]['name']
    elif player_two_choice in wwr_options[player_one_choice]['beats']:
        winner = 'player'
        reason = wwr_options[player_one_choice]['beats'][player_two_choice]
    else:
        winner = 'computer'
        reason = wwr_options[player_two_choice]['beats'][player_one_choice]
    if print_reason:
        print(reason)
    return winner


def computer_turn(ct_options):
    """Random choice for the computer player"""
    turn = str(random.choices(list(ct_options.keys()))[0])
    return turn


def play_round(scores, pr_options, prompt):
    """Play a round"""
    player_one_turn = ''
    while player_one_turn not in pr_options:
        player_one_turn = str(input(prompt)[0])
        if player_one_turn not in pr_options:
            print("Sorry, " + prompt)
    player_two_turn = computer_turn(pr_options)
    print("Computer played " + player_two_turn)
    winner = who_won_round(player_one_turn, player_two_turn, pr_options)
    scores[winner] += 1
    print(winner + " won this round")
    return scores


def game():
    """The actual game!"""
    which_game = input("Do you want to play the expanded version?  y/n: ")
    if which_game.lower() == 'y':
        options = get_options('bbt')
    else:
        options = get_options('normal')
    prompt = options['prompt']
    options.popitem()
    scores = {
        'player': 0,
        'computer': 0,
        'no one': 0
    }
    play_again = True
    while play_again:
        # noinspection PyTypeChecker
        scores = play_round(scores, options, prompt)
        answer = input("type y to play again: ")
        if answer[0].lower() == 'y':
            play_again = True
        else:
            play_again = False
    print(
        "Player won " + str(scores['player']) + " and computer won " + str(scores['computer']) + '.  There were ' + str(
            scores['no one']) + ' draws.')


game()
