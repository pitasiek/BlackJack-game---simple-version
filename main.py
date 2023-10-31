# Made by Piotr Zięba on 31.10.2023. It is a Black Jack game.
# I finish this project a little bit late because I took a break from the bootcamp to finish classes from Mimo.
# I admit that this project was quite tricky to finish.
from art import logo    # Logo for the game.
import random


def deal_card():
    # Function that selects one card from the deck and returns it.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Available cards.
    card = random.choice(cards)    # Random pick.
    return card


def calculate_score(points):
    # Function checks for blackjack and takes care of ace as it can be 11 or 1 based on the circumstance.
    if sum(points) == 21 and len(points) == 2:
        return 21    # Blackjack!
    if 11 in points and sum(points) > 21:    # Over 21 ace becomes 1.
        points.remove(11)
        points.append(1)
    return sum(points)    # We get the sum of points to know what decision to do next.


def blackjack_game():
    # System for the game.
    print(logo)
    user_cards = []  # User's cards
    dealer_cards = []  # Computer's cards.
    for index in range(2):  # 'For' loop that appends points to lists above.
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    first_loop = 0    # First and first_2 loop appear bellow inside 'decision' while loop.
    first_2_loop = 0
    decision = "y"    # Decision to take another card.
    total_dealer = 0
    total_player = 0
    while decision == "y":
        if first_loop == 0:
            total_player = calculate_score(user_cards)  # Calculates total points.
            total_dealer = calculate_score(dealer_cards)
            print(f"Your cards are {user_cards[0]} and {user_cards[1]}. Your current score is {total_player}.")
            print(f"Dealer has got {dealer_cards[0]} and a hidden card.")
            first_loop += 1
        if total_dealer == 21 or total_player > 21:
            print("###########")
            print(f"You lose!!! You have got {total_player} points and dealer has got {total_dealer}.")
            print("###########")
            return
        elif total_player == 21 or total_dealer > 21:
            print("###########")
            print(f"You win!!! You have got {total_player} points and dealer has got {total_dealer}.")
            print("###########")
            return
        decision = input("Do you want to take another card? 'y' or 'n'")
        if decision == "y":
            user_cards.append(deal_card())
            total_player = calculate_score(user_cards)
            print(f"Your card is {user_cards[-1]}. Your current score is {total_player}.")
        elif decision == "n":
            while total_dealer < 17:
                dealer_cards.append(deal_card())
                total_dealer = calculate_score(dealer_cards)
                if first_2_loop == 0:
                    print(f"Dealer's hidden card was {dealer_cards[1]}!!!")
                    first_2_loop += 1
                print(f"Dealer's new card is {dealer_cards[-1]}. Dealer's current score is {total_dealer}.")
                if (total_dealer >= 17) and (total_dealer > total_player) and (total_dealer <= 21):
                    print("###########")
                    print("You lose!!!")
                    print("###########")
                    return
                elif (total_dealer >= 17) and (total_dealer < total_player):
                    print("###########")
                    print(f"You win! You have got more points than the dealer.")
                    print("###########")
                    return
                elif total_dealer == total_player:
                    print("###########")
                    print(f"It is a tie!!! Final points are {total_dealer} and {total_dealer}")
                    print("###########")
                    return
                elif (total_dealer >= 17) and (total_dealer > 21):
                    print("###########")
                    print(f"You win!!! You have got {total_player} points and dealer has got {total_dealer}.")
                    print("###########")
                    return


# ----------Game starts here ----------
again = True
while again:    # Loop that allows the player to play again.
    start = input("Do you want to play blackjack? 'y' or 'n'")
    if start == "y":
        blackjack_game()
    else:
        again = False    # Gets false to stop the loop and end the game.
        input("Good bye!")
