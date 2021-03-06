#!/usr/bin/env python3
# Chris Fergo Jr presents: Rock, Paper, Scissors: Video Game

import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock, scissors: paper }

player_score = 0
computer_score = 0

def start():
    print ("I am Stone Head, the third henchman of Jenkin the Great. I will let you pass by if you win three Jenkin matches.")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print ("You must choose either paper, scissors, or rock. Plese enter 1, 2 or 3.")

def result(player, computer):
    print ("1...")
    time.sleep(1)
    print ("2...")
    time.sleep(1)
    print ("3!")
    time.sleep(0.5)
    print ("Computer threw (0)!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print ("It's a draw.")
    else:
        if rules[player] == computer:
            print ("Well it looks like that's the way it's meant to be.")
            player_score += 1
        else:
            print ("You lose.")
            computer_score += 1

def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print ("You lost and have been turned to stone! Thanks for playing!")

def scores():
    global player_score, computer_score
    print ("HIGH SCORES")
    print ("Player: ", player_score)
    print ("Computer: ", computer_score)

    if __name__ == '__main__':
        start()
        
    
