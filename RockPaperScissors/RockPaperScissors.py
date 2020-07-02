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
    elif player_one_choice == 's':
        if player_two_choice == 'r':
            winner = 'computer'
        elif player_two_choice == 's':
            winner = 'no one'
        elif player_two_choice == 'p':
            winner = 'player'
    elif player_one_choice == 'p':
        if player_two_choice == 'r':
            winner = 'player'
        elif player_two_choice == 's':
            winner = 'computer'
        elif player_two_choice == 'p':
            winner = 'no one'
    return winner


def computer_turn():
    """Random choice for the computer player"""
    turn = random.choices(['rock', 'paper', 'scissors'])
    print("Computer played " + turn[0])
    return turn[0][0]


def play_round(scores):
    """Play a round"""
    player_one_turn = ''
    while player_one_turn not in ['r', 's', 'p']:
        player_one_turn = input("please enter r for rock, s for scissors, or p for paper: ")
        if player_one_turn not in ['r', 's', 'p']:
            print("Sorry, please enter r or s or p")
    player_two_turn = computer_turn()
    winner = who_won_round(player_one_turn, player_two_turn)
    scores[winner] += 1
    print(winner + " won this round")
    return scores


def game():
    """The actual game!"""
    scores = {
        'player': 0,
        'computer': 0,
        'no one': 0
    }
    play_again = True
    while play_again:
        scores = play_round(scores)
        answer = input("type y to play again: ")
        if answer[0].lower() == 'y':
            play_again = True
        else:
            play_again = False
    print(
        "Player won " + str(scores['player']) + " and computer won " + str(scores['computer']) + '.  There were ' + str(
            scores['no one']) + ' draws.')


game()
