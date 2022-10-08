import random
from words import word_list
def main():
    LIMIT = 8
    answers = [f"Find the word in less than {LIMIT} guesses. Good luck!\n", "Correct!\n", "Wrong guess.\n",
               "Wrong input. Type a single letter or 'exit'\n", "You already tried that letter.\n"]
    word = random.choice(word_list).upper()
    wrong_guesses = []
    eval_guess = 0  # index for the 'answers' list
    outcome =""
    last_tried = ""  # last letter tried
    # build hidden word:
    hidden_word = ["_" for i in range(len(word))]

    # Prints the hangman progress, default value is zero
    def display_hangman(counter):
        if counter == 1:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |    \n', '   |  \n', '   |   \n',
                                                          '  |\n', '|\n'))
            # the :^ Center aligns the result (within the available space)
            # so the first {:^34 } will be formatted to the "____\n" to align it to the center
        elif counter == 2:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \n', '   |   \n',
                                                          '  |\n', '|\n'))
        elif counter == 3:
            print(
                "{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \\\n', '   |   \n',
                                                        '  |\n', '|\n'))
        elif counter == 4:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \\|\n',
                                                          '   |   \n', '  |\n', '|\n'))
        elif counter == 5:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \\|/\n',
                                                          '   |   \n', '  |\n', '|\n'))
        elif counter == 6:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \\|/\n',
                                                          '   |   |\n', '   |\n', '|\n'))
        elif counter == 7:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \\|/\n',
                                                          '   |   |\n', '   |  / \n', '|\n'))
        elif counter == 8:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   |\n', '   |   O\n', '   |  \\|/\n',
                                                          '   |   |\n', '   |  / \\\n', '|\n'))
        else:
            print("{:^34}{}{:^31}{}{:^31}{}{:^30}".format(' _____\n ', '|   \n', '   |    \n', '   |  \n', '   |   \n',
                                                          '  |\n', '|\n'))
            # this is to print the hang stand when the user has not guessed yet

    # display the messages of the game
    def display_messages(wrong_guesses, hidden_word, eval_guess=0, LIMIT=8, outcome="", last_tried=""):
        display_hangman(len(wrong_guesses))
        if outcome == 1:
            print(f"{'YOU WIN!':^36}\nYou rightly guessed: {word}")
            print("\nYou also tried: ", wrong_guesses)
            play_loop()
        elif outcome == 0:
            print(f"{'GAME OVER.':^36}\n{'The word was:':^15}{word}")
            print("\nYou guessed:", hidden_word, "\nYou tried:", wrong_guesses)
            play_loop()
        else:
            print(hidden_word, "\n")
            print(f"{answers[eval_guess]}")
            print(f"Wrong guesses: {wrong_guesses} Wrong guesses remaining: {LIMIT - len(wrong_guesses)}")
            print(f"Length: {len(hidden_word)} last letter tried: {last_tried}")


    # core of the game
    while True:
        if len(wrong_guesses) == LIMIT:
            display_messages(wrong_guesses, hidden_word, outcome=0)
            break
        if "_" not in hidden_word:
            display_messages(wrong_guesses, hidden_word, outcome=1)
            break
        # messages function
        display_messages(wrong_guesses, hidden_word, eval_guess, LIMIT, outcome, last_tried)
        # user interaction
        prompt = input("Pick a letter or type 'exit' to quit: ").upper()  # make input uppercase regardless
        if prompt.upper() == "EXIT":
            print("Bye.")
            break
        if prompt.isalpha() and len(prompt) == 1:  # check if input single letter
            # the .isaplha method returns True if all the characters are alphabet letters
            if prompt in wrong_guesses or prompt in hidden_word:  # If letter already tried
                eval_guess = 4  # this calls the 4th index of answer variable(you already tried that)
            elif prompt in word:  # correct guess
                last_tried = prompt  # update last tried letter
                eval_guess = 1  # set the answer to 'Correct!'
                for i in range(len(word)):
                    if prompt == word[i]:
                        hidden_word[i] = prompt  # replace "_" with the letter
            elif prompt not in wrong_guesses:  # Wrong guess. Add wrong letter to the wrong guesses list
                eval_guess = 2  # set the answer to 'Wrong guess!'
                wrong_guesses.append(prompt)
                last_tried = prompt
        else:
            eval_guess = 3  # wrong input'
def play_loop():
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game.upper() == "Y":
        main()
    elif play_game.upper() == "N":
        print("Thanks For Playing!")
        exit()
main()