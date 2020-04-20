player1 = input("Player 1 enter your choice: ")
player2 = input("Player 2 enter your choice: ")

if player1.lower() == "rock" and player2.lower() == "paper":
    print("Player 2 is the winner")
elif player1.lower() == "paper" and player2.lower() == "rock":
    print("Player 1 is the winner")
elif player1.lower() == "scissors" and player2.lower() == "rock":
    print("Player 2 is the winner")
elif player1.lower() == "rock" and player2.lower() == "sciccors":
    print("Player 1 is the winner")
elif player1.lower() == "paper" and player2.lower() == "scissors":
    print("Player 2 is the winner")
elif player1.lower() == "scissors" and player2.lower() == "paper":
    print("Player 1 is the winner")
elif player1.lower() == player2.lower():
    print("It is a draw")