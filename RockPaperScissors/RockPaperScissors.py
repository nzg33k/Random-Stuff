"""Rock, Paper, Scissors"""
import random


def who_won_round(player_one_choice, player_two_choice):
    """Figure out who won"""
    winner = ""
    if player_one_choice == 'r':
        if player_two_choice == 'r':
            winner = 'no one'
        elif player_two_choice == 's':
            winner = 'player'
        elif player_two_choice == 'p':
            winner = 'computer'
        elif player_two_choice == 'l':
            winner = 'player'
        elif player_two_choice == 'v':
            winner = 'computer'
    elif player_one_choice == 's':
        if player_two_choice == 'r':
            winner = 'computer'
        elif player_two_choice == 's':
            winner = 'no one'
        elif player_two_choice == 'p':
            winner = 'player'
        elif player_two_choice == 'l':
            winner = 'player'
        elif player_two_choice == 'v':
            winner = 'computer'
    elif player_one_choice == 'p':
        if player_two_choice == 'r':
            winner = 'player'
        elif player_two_choice == 's':
            winner = 'computer'
        elif player_two_choice == 'p':
            winner = 'no one'
        elif player_two_choice == 'l':
            winner = 'computer'
        elif player_two_choice == 'v':
            winner = 'player'
    elif player_one_choice == 'l':
        if player_two_choice == 'r':
            winner = 'computer'
        elif player_two_choice == 's':
            winner = 'player'
        elif player_two_choice == 'p':
            winner = 'computer'
        elif player_two_choice == 'l':
            winner = 'no one'
        elif player_two_choice == 'v':
            winner = 'player'
    elif player_one_choice == 'v':
        if player_two_choice == 'r':
            winner = 'player'
        elif player_two_choice == 's':
            winner = 'player'
        elif player_two_choice == 'p':
            winner = 'computer'
        elif player_two_choice == 'l':
            winner = 'computer'
        elif player_two_choice == 'v':
            winner = 'no one'
    return winner


def computer_turn(options):
    """Random choice for the computer player"""
    turn = random.choices(options)
    print("Computer played " + turn[0])
    return turn[0][0]


def play_round(scores, options):
    """Play a round"""
    player_one_turn = ''
    if len(options) == 3:
        prompt = "please enter r for rock, s for scissors, or p for paper: "
    elif len(options) == 5:
        prompt = "please enter r for rock, s for scissors, p for paper, l for lizard, or v for (Vulcan) Spock: "
    while player_one_turn not in options:
        player_one_turn = input(prompt)
        if player_one_turn not in options:
            print("Sorry, " + prompt)
    player_two_turn = computer_turn(options)
    winner = who_won_round(player_one_turn, player_two_turn)
    scores[winner] += 1
    print(winner + " won this round")
    return scores


def game():
    """The actual game!"""
    which_game = input("Do you want to play the expanded version?  y/n: ")
    if which_game.lower() == 'y':
        options = ['r', 'p', 's', 'l', 'v']
    else:
        options = ['r', 'p', 's']
    scores = {
        'player': 0,
        'computer': 0,
        'no one': 0
    }
    play_again = True
    while play_again:
        scores = play_round(scores, options)
        answer = input("type y to play again: ")
        if answer[0].lower() == 'y':
            play_again = True
        else:
            play_again = False
    print(
        "Player won " + str(scores['player']) + " and computer won " + str(scores['computer']) + '.  There were ' + str(
            scores['no one']) + ' draws.')


game()
