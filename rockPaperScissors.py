import random
import time

available = ["rock", "paper", "scissors"]
ai_inv = ["Rock", "Paper", "Scissors"]
player_score = 0
ai_score = 0
over = False

def game():

    global player_score, ai_score, over

    player_attack = input("Choose your attack: ")
    if player_attack in available:
        ai_attack = random.choice(ai_inv)

        time.sleep(1)
        print("Rock, Paper, Scissors...")
        time.sleep(1)
        print("Shoot!")
        print(player_attack.capitalize())
        print(ai_attack)
        time.sleep(1)

        if player_attack == available[0] and ai_attack == ai_inv[0]:
            print("Tie!")
        elif player_attack == available[1] and ai_attack == ai_inv[0]:
            print("Player wins!")
            player_score += 1
        elif player_attack == available[0] and ai_attack == ai_inv[1]:
            print("AI wins!")
            ai_score += 1
        elif player_attack == available[1] and ai_attack == ai_inv[1]:
            print("Tie!")
        elif player_attack == available[2] and ai_attack == ai_inv[1]:
            print("Player wins!")
            player_score += 1
        elif player_attack == available[2] and ai_attack == ai_inv[2]:
            print("Tie!")
        elif player_attack == available[2] and ai_attack == ai_inv[0]:
            print("AI wins!")
            ai_score += 1
        elif player_attack == available[0] and ai_attack == ai_inv[2]:
            print("Player wins!")
            player_score += 1
        elif player_attack == available[1] and ai_attack == ai_inv[2]:
            print("AI wins!")
            ai_score += 1

        if player_score >= 3:
            print("PLAYER WINS ROCK PAPER SCISSORS!!!")
            print(f"Player score: {player_score}")
            print(f"AI score: {ai_score}")
            over = True
        elif ai_score >= 3:
            print("AI WINS ROCK PAPER SCISSORS!!!")
            print(f"AI score: {ai_score}")
            print(f"Player score: {player_score}")
            over = True
        return
    else:
        print("Invalid, must be Rock, Paper, or Scissors.")
        game()

while over == False:
    game()