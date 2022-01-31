# Imports
from art import logo, vs
from game_data import data
import random
from replit import clear


def new_game():

    # User score start at 0
    user_score = 0
    # The end of game is not true
    end_of_game = False

    def intro_screen():
        """Intro screen"""
        # Intro
        print(logo)
        print("\nWHO HAS THE MOST FOLLOWERS?")
        print(
            "\n--------------------------------------------------------------------------------"
        )
        print("By:        Armand van der Merwe")
        print("Contact:   arri.vdm@gmail.com")
        print(
            "--------------------------------------------------------------------------------"
        )

    while end_of_game == False:

        clear()

        # Show intro
        intro_screen()

        # Get two random dictionaries from list
        record_one = random.choice(data)
        record_two = random.choice(data)

        # If the two records are the same, generate a new
        # record and assign it to the second record
        def alt_dict(dict_1, dict_2):
            """Ensure that you never have two dictionaries
            which are the same: e.g. record_one = record_two.
            - IF THE TWO DICTIONARIES ARE THE SAME: 
            - Generate a new dictionary assign it to record_two
            """
            if dict_1 == dict_2:
                while dict_1 == dict_2:
                    alternative = random.choice(data)
                    dict_2 = alternative
                    return dict_2
            else:
                return dict_2

        record_two = alt_dict(dict_1=record_one, dict_2=record_two)

        # How many followers?
        record_one_followers = record_one['follower_count']
        record_two_followers = record_two['follower_count']

        if user_score >= 1:
            print(f"\nYou're RIGHT! Current SCORE: {user_score}")

        # Testing
        # print(f"record_one_followers = {record_one_followers}")
        # print(f"record_two_followers {record_two_followers}")

        # Display the dictionaries
        def display():
            """Displays the two records"""
            # Record 1
            print(
                f"\nCompare 1:\n---------\n{record_one['name']}, {record_one['description']},\nfrom {record_one['country']}."
            )
            # Display: vs
            print(vs)
            # Record 2
            print(
                f"\nAgainst 2:\n---------\n{record_two['name']}, {record_two['description']},\nfrom {record_two['country']}.\n"
            )

        display()

        # Ask the user who has more followers
        print(
            "--------------------------------------------------------------------------------\n"
        )
        user_choice = int(input("Who has more followers? Type '1' or '2'\n"))

        # Compare user choice with followers
        def update_score(user_score):
            """Compare user choice with followers"""

            if \
            (record_one_followers > record_two_followers and user_choice == 1) \
            or \
            (record_two_followers > record_one_followers and user_choice == 2):
                user_score += 1
                return user_score
            else:
                user_score = 0
                return user_score

        user_score = update_score(user_score=user_score)

        def game_end():
            if user_score >= 1:
                end_of_game = False
                return end_of_game
            elif user_score == 0:
                clear()
                intro_screen()
                print(f"\nSorry, that's wrong!")
                restart = input(
                    "\nWould you like to play again?\nEnter 'y' for YES, or...\nEnter 'n' for NO, or...\n"
                ).lower()
                if restart in ("y", "yes"):
                    clear()
                    new_game()
                else:
                    end_of_game = True
                    clear()
                    intro_screen()
                    print("\nThank you for playing!\nGoodbye...\n\n")
                    return end_of_game

        end_of_game = game_end()


new_game()
