# File: Hangman
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E

import random



def play_hangman():
    """
    Plays hangman with the user using user inputs. User either wins or loses. 

    :secret_word: String. Word chosen by computer to be guessed. Used throuhgout the code to check if the user's 
    guess is valid or if the user won/lost.

    :guessed_word: String. Word displayed which displays the part of the word that has been correctly guessed.
    Blank spaces are filled with hyphens.

    :try_count: Integer. The number of tries remaining. 1 is Deducted for each letter guessed not in secret_word.
    User loses if this hits 0; they run out of tries.

    :entered_letters: List. if a letter is guessed, either in or not in secret_word, it is appended to 
    entered_letters, this is used to check if a user is re-guessing a letter.

    :guessed_word: String. The user's input and what the program uses to identify if they've correctly guessed
    the letters in secret_word.

    :No Return: Function does not return anything
    """

    # initialize variables
    word_list = ['grip', 'suspend', 'reward', 'list', 'evolve', 'leap', 'provide', 'launch', 'proclaim' \
                'phobic', 'home', 'shallow', 'supreme', 'lacking', 'petite', 'weak', 'bent', 'resonant' \
                'user', 'office', 'housing', 'orange', 'fortune', 'length', 'wife', 'series', 'bedroom', 'actor']
    word = random.randint(0, 28)
    secret_word = word_list[word]
    guessed_word = '-' * len(secret_word)
    try_count = 8
    entered_letters = []

    print('Let\'s play hangman!')
    print(guessed_word)

    # core function of play_hangman. Gives output for each possible user guess
    # while loop keeps game running so long as loser hasn't lost. 
    playing = True
    while playing: 
        while guessed_word != secret_word and try_count > 0:

            user_input = str.lower(input('Guess a letter: '))

            # makes sure user guess is a single string that isn't a number or special character
            if len(user_input) == 1 and user_input.isalpha():

                # checks if the user's letter has already been guessed, adds it to list if it's a new letter
                if user_input in entered_letters:
                        print(f'You\'ve already guessed {user_input}')

                elif user_input in secret_word:                    
                    entered_letters.append(user_input)
                    
                    # checks to see if the letter the user guessed is in secret_word. If yes, the guessed_word string
                    # is sliced to put the new letter in each applicable place, otherwise try count goes down. Prints
                    # the number of try counts and the guessed word reguardless of if the user guessed the correct thing
                    for i in range(len(secret_word)):
                            
                        if user_input == secret_word[i]:
                            first = guessed_word[:i]

                            if i + 1 < len(secret_word):
                                second = guessed_word[i + 1:]
                                guessed_word = first + user_input + second

                            else:
                                guessed_word = first + user_input
                                
                            print(guessed_word)

                            if guessed_word != secret_word:
                                print(f'You have {try_count} tries remaining.')   
                                print() 
                else:
                    try_count -= 1

                    entered_letters.append(user_input)
                    print(guessed_word)

                    if guessed_word != secret_word:
                        print(f'You have {try_count} tries remaining.')
                        print()    
            
                # check conditions for while loop to determine if user won or lost or game keeps playing
                if try_count == 0:
                    print('You lose.')

                elif guessed_word == secret_word:
                    print('You win!')
                                        
            else: 
                print('That is not a letter. Enter a letter.')

        play_again = input("Do you want to play again? y/n ")
        if play_again != 'y':
            playing = False


"""
Driver Code
"""

def main():
    play_hangman()
    
if __name__ == '__main__':
    main()