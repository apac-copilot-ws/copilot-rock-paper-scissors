# write a rock, paper, scissors game
# import random module
import random
#define main function that handles the logic of the game
def main():
    # define variables
    # set counter to 0
    counter = 0
    # set user_wins to 0
    user_wins = 0
    # set computer_wins to 0
    computer_wins = 0
    # set ties to 0
    ties = 0
    # create a list of options for the computer to choose from
    options = ['rock', 'paper', 'scissors']
    # create a loop that runs 10 times
    while counter < 10:
        # get the user's choice
        user_choice = input('Enter rock, paper, or scissors: ')
        # get the computer's choice
        computer_choice = random.choice(options)
        # display the computer's choice
        print('Computer chose:', computer_choice)
        # display the winner of the round
        if user_choice == 'rock' and computer_choice == 'scissors':
            print('You win!')
            user_wins += 1
        elif user_choice == 'rock' and computer_choice == 'paper':
            print('Computer wins!')
            computer_wins += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('You win!')
            user_wins += 1
        elif user_choice == 'paper' and computer_choice == 'scissors':
            print('Computer wins!')
            computer_wins += 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('You win!')
            user_wins += 1
        elif user_choice == 'scissors' and computer_choice == 'rock':
            print('Computer wins!')
            computer_wins += 1
        else:
            print('It\'s a tie!')
            ties += 1
        # increment the counter
        counter += 1
    # display the number of wins, losses, and ties
    print('You won', user_wins, 'times.')
    print('The computer won', computer_wins, 'times.')
    print('There were', ties, 'ties.')

    # call main function
main()

