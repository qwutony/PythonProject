#!/usr/bin/python3

# This project aims to create a simple heads-up Texas Holdem poker game between the user (player) and the opponent (simple AI). 
# It is a game that involves a deck of cards, money, probability and psychology. 

# Imports the random module for future use
import random

# Imports the os module (currently used only to clear screen)
import os

# Clears screen to maximise readability
def clear():
    os.system('clear')

# Initiate a card class with parameters court (face) and suit
class card():

    # The class card requires an input of court and suit parameters
    def __init__(self, court, suit):
        self.court = court
        self.suit = suit
        
class player():
    
    # The class player requires an input of stack parameter for starting value
    def __init__(self, stack):
        self.stack = stack

    # Created a method within the player class to allow for betting.
    def bet(self, player, pot):
        # Betting aspect of the game, should be kept under a single umbrella
        bet = input("How much would you like to bet? ")
        # Initially converts input strings into integer
        while int(bet) > player.stack:
            bet = input("You do not have enough chips. Please select another value to bet. ")
            if int(bet) <= player.stack:
                break
        if int(bet) == player.stack:
            print("ALL IN!")
            pot = pot + player.stack
            player.stack = 0
        elif int(bet) < player.stack:
            print("You have bet", bet, "!")
            pot = pot + int(bet)
            player.stack = player.stack - int(bet)
        else:
            print("You have decided to check.")
        print(player.stack)
        print(pot)
        return pot

    def check(self, check):
        self.check = check
        if check == True:
            print("You have decided to check.")

    def call(self, money):
        self.call = call
    
    def fold(self):
        #####
        new_game()

# Create a function wrapper responsible for creating a new deck and dealing the cards to the respective player
def new_game():
        
    # Creates an array containing four suits
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    
    # Creates an array with all the court (face) cards
    courts = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Trey', 'Deuce']

    # Initiate an empty array for a deck
    deck = []

    # Create a for loop to create a deck with varying courts and suits
    for court in courts:
        for suit in suits:
            # A temporary variable (cards) is generated that will store the card values
            cards = card(court, suit)
            # Storing the values from temp into the deck array using .append
            deck.append(cards)

    # Create an empty array to store 9 cards for the game
    rand_num = []

    # Initialise for loop that takes all the integers from 9 random numbers between 1 and 52 and stores it into the rand_num array
    for int in random.sample(range(0, 52), 9):
        rand_num.append(int)

    # Print function of rand_num array for debugging
    print(rand_num)

    # Informing the player of the cards that s/he is dealt
    print("Your cards are the", deck[rand_num[0]].court, "of", deck[rand_num[0]].suit, "and the", deck[rand_num[1]].court, "of", deck[rand_num[0]].suit + ".")

    # Print function of opponents cards for debugging
    print("Your opponent's cards are the", deck[rand_num[2]].court, "of", deck[rand_num[2]].suit, "and the", deck[rand_num[3]].court, "of", deck[rand_num[3]].suit + ".")

    # Clear pot value from previous game, if any
    pot = 0

    # Initiates a player with a stack size of 50 chips 
    name = player(50)

    # Allows the player to bet, comparing the bet size with the stack size
    bet_value = name.bet(name, pot)

    # Debugging the value of pot, but for some reason is returning 0
    print(bet_value)

    # Debugging by passing the value of check
    name.check(True)

# def flop():

#     while name.fold != True


# Insert some simple welcoming messages
print("Welcome to Sellout Casino! A place where dreams come true (but not yours!)\n")

# Create a variable to store the player name, which will be used in the future
name = input("What is your name? ")
clear()

# Another welcome message
print("Welcome", name + "!\n" + "Thank you for joining us today! Here are 50 chips! Good Luck and may the odds be ever in your favor!")

# Function signalling the beginning of a new game
new_game()

