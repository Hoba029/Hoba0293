# File : CS112_A1_T2_Game3_20231106
"""
# Purpose :  This is a two-player mathematical game of strategy. It is played by two 
people with a pile of coins (or other tokens) between them. The players take turns removing 
coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). 
The player who removes the last coin wins.
"""
# Author : Abdelwahab Essam Mohamed Abdelwahab
# ID : 20231106



# Welcoming message for the players
print("Hello! Welcome to Subtract a square game!")

# Asking the players for their names
first_player_name= str(input("Enter a name for first player"))
second_player_name= str(input("Enter a name for second player"))

# Asking players to choose a number to start from
starting_number=int(input("Please, enter a number to start from"))

#The counter decides the winner
counter= 0

# Assuming that i=1 just to define the variable i before starting the loop
i=0
while starting_number >0:
        
        # Asking the player to choose a number to subtract it from the starting
        i = int(input(f" Please, enter a square to subtract if from {starting_number} "))
        
        # IF a player adds a not squared number, the program ask them to try again with a squared number
        if i**(1/2)%1!=0:
            print("Please, enter a squared number")    
        
        # If a player adds a squared number the game keeps subtracting the number from the starting number until one player reaches 0 and win
        if i**(1/2)%1==0:            
            starting_number= starting_number-i
            counter= counter+1
        
        if starting_number ==0:
            print("Game over!")

            # If the first player chooses a squared number fot their first time, the counter turns from 0 to 1. 
            # If the second player chooses a squared number fot their first time, the counter turns from 1 to 2.
            # So if the counter is odd, then the player who played last is the first player and supposed to be the winner.
            if counter %2!=0:
                print(first_player_name, " is the winner!")
                break
            
            #And if the counter is even, then the player who played last is the second player and supposed to be the winner.
            if counter %2==0:
                print(second_player_name, " is the winner!")
                break

