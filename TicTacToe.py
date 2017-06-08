## TicTacToe.py
##
## This program will enable 2 players to play tic-tac-toe using standard rules.
##
## Aster Fan
##
## June 2017

# State intention of this program.
print("\nThis is a 2-player Tic-Tac-Toe program.\n")

# These are the variables that are placed on the game board, changing based on user input. 
topLeft = " "
topCenter = " "
topRight = " "

middleLeft = " "
middleCenter = " "
middleRight = " "

bottomLeft = " "
bottomCenter = " "
bottomRight = " "

# This will be the board that the help users coordinate the placement of their X's and O's.
print("\t\t\t\t|1|  |2|  |3|\n\n\t\t\t\t|4|  |5|  |6|\n\n\t\t\t\t|7|  |8|  |9|")

# This statement tells the users that whoever goes first will be the X's.
print("\n\n\nThe player going first will be the X's. The other player will be the O's")

while True:
# X User input will now start. The code below will place the X where the user decides.
    while True:
        userDecision = input("\nPLAYER X: \nUsing the numbered board as guidance, type in the number to indicate where you want your first X: ")
        if "1" in userDecision:
            topLeft = "X"
            break
        elif "2" in userDecision:
            topCenter = "X"
            break
        elif "3" in userDecision:
            topRight = "X"
            break
        elif "4" in userDecision:
            middleLeft = "X"
            break
        elif "5" in userDecision:
            middleCenter = "X"
            break
        elif "6" in userDecision:
            middleRight = "X"
            break
        elif "7" in userDecision:
            bottomLeft = "X"
            break
        elif "8" in userDecision:
            bottomCenter = "X"
            break
        elif "9" in userDecision:
            bottomRight = "X"
            break
        else:
            print("\nInvalid. Try again.")

# This print statement will print out the result.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))

# O user input will now start. The code below is similar to the one above.            
    while True:
        userDecision = input("\nPLAYER O: \nUsing the numbered board as guidance, type in the number to indicate where you want your first O: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "O"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "O"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "O"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "O"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "O"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "O"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "O"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "O"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "O"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 2nd move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))

# X user input, 2nd turn.
    while True:
        userDecision = input("\nPLAYER X: \nUsing the numbered board as guidance, type in the number to indicate where you want your X: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "X"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "X"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "X"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "X"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "X"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "X"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "X"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "X"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "X"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 3rd move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))

# O user input, 2nd turn.            
    while True:
        userDecision = input("\nPLAYER O: \nUsing the numbered board as guidance, type in the number to indicate where you want your O: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "O"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "O"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "O"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "O"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "O"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "O"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "O"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "O"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "O"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 4th move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))

# X user input, 3rd turn.
    while True:
        userDecision = input("\nPLAYER X: \nUsing the numbered board as guidance, type in the number to indicate where you want your X: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "X"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "X"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "X"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "X"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "X"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "X"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "X"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "X"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "X"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 5th move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))
    

# We have to check the win condition now (3 X's or O's in a row)
    if "X" in topLeft and "X" in topCenter and "X" in topRight:
        print("The winner is player X!")
        break
    elif "X" in middleLeft and "X" in middleCenter and "X" in middleRight:
        print("The winner is player X!")
        break
    elif "X" in bottomLeft and "X" in bottomCenter and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topLeft and "X" in middleLeft and "X" in bottomLeft:
        print("The winner is player X!")
        break
    elif "X" in topCenter and "X" in middleCenter and "X" in bottomCenter:
        print("The winner is player X!")
        break
    elif "X" in topRight and "X" in middleRight and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topLeft and "X" in middleCenter and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topRight and "X" in middleCenter and "X" in bottomLeft:
        print("The winner is player X!")
        break
    else:
        pass

# O user input, 3rd turn.            
    while True:
        userDecision = input("\nPLAYER O: \nUsing the numbered board as guidance, type in the number to indicate where you want your O: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "O"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "O"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "O"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "O"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "O"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "O"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "O"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "O"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "O"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 6th move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))

# Checking win condition (3 X's or O's in a row)
    if "O" in topLeft and "O" in topCenter and "O" in topRight:
        print("The winner is player O!")
        break
    elif "O" in middleLeft and "O" in middleCenter and "O" in middleRight:
        print("The winner is player O!")
        break
    elif "O" in bottomLeft and "O" in bottomCenter and "O" in bottomRight:
        print("The winner is player O!")
        break
    elif "O" in topLeft and "O" in middleLeft and "O" in bottomLeft:
        print("The winner is player O!")
        break
    elif "O" in topCenter and "O" in middleCenter and "O" in bottomCenter:
        print("The winner is player O!")
        break
    elif "O" in topRight and "O" in middleRight and "O" in bottomRight:
        print("The winner is player O!")
        break
    elif "O" in topLeft and "O" in middleCenter and "O" in bottomRight:
        print("The winner is player O!")
        break
    elif "O" in topRight and "O" in middleCenter and "O" in bottomLeft:
        print("The winner is player O!")
        break
    else:
        pass

# X user input, 4th turn.
    while True:
        userDecision = input("\nPLAYER X: \nUsing the numbered board as guidance, type in the number to indicate where you want your X: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "X"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "X"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "X"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "X"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "X"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "X"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "X"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "X"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "X"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 7th move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))
    

# Checking win condition (3 X's or O's in a row)
    if "X" in topLeft and "X" in topCenter and "X" in topRight:
        print("The winner is player X!")
        break
    elif "X" in middleLeft and "X" in middleCenter and "X" in middleRight:
        print("The winner is player X!")
        break
    elif "X" in bottomLeft and "X" in bottomCenter and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topLeft and "X" in middleLeft and "X" in bottomLeft:
        print("The winner is player X!")
        break
    elif "X" in topCenter and "X" in middleCenter and "X" in bottomCenter:
        print("The winner is player X!")
        break
    elif "X" in topRight and "X" in middleRight and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topLeft and "X" in middleCenter and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topRight and "X" in middleCenter and "X" in bottomLeft:
        print("The winner is player X!")
        break
    else:
        pass

# O user input, 4th turn.            
    while True:
        userDecision = input("\nPLAYER O: \nUsing the numbered board as guidance, type in the number to indicate where you want your O: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "O"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "O"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "O"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "O"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "O"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "O"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "O"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "O"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "O"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 8th move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))

# Checking win condition (3 X's or O's in a row)
    if "O" in topLeft and "O" in topCenter and "O" in topRight:
        print("The winner is player O!")
        break
    elif "O" in middleLeft and "O" in middleCenter and "O" in middleRight:
        print("The winner is player O!")
        break
    elif "O" in bottomLeft and "O" in bottomCenter and "O" in bottomRight:
        print("The winner is player O!")
        break
    elif "O" in topLeft and "O" in middleLeft and "O" in bottomLeft:
        print("The winner is player O!")
        break
    elif "O" in topCenter and "O" in middleCenter and "O" in bottomCenter:
        print("The winner is player O!")
        break
    elif "O" in topRight and "O" in middleRight and "O" in bottomRight:
        print("The winner is player O!")
        break
    elif "O" in topLeft and "O" in middleCenter and "O" in bottomRight:
        print("The winner is player O!")
        break
    elif "O" in topRight and "O" in middleCenter and "O" in bottomLeft:
        print("The winner is player O!")
        break
    else:
        pass

# X user input, 5th turn.
    while True:
        userDecision = input("\nPLAYER X: \nUsing the numbered board as guidance, type in the number to indicate where you want your X: ")
        if "1" in userDecision and " " in topLeft:
            topLeft = "X"
            break
        elif "2" in userDecision and " " in topCenter:
            topCenter = "X"
            break
        elif "3" in userDecision and " " in topRight:
            topRight = "X"
            break
        elif "4" in userDecision and " " in middleLeft:
            middleLeft = "X"
            break
        elif "5" in userDecision and " " in middleCenter:
            middleCenter = "X"
            break
        elif "6" in userDecision and " " in middleRight:
            middleRight = "X"
            break
        elif "7" in userDecision and " " in bottomLeft:
            bottomLeft = "X"
            break
        elif "8" in userDecision and " " in bottomCenter:
            bottomCenter = "X"
            break
        elif "9" in userDecision and " " in bottomRight:
            bottomRight = "X"
            break
        else:
            print("\nInvalid. Try again.")

# Result from 9th move of the game.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))
    

# Checking win condition (3 X's or O's in a row)
    if "X" in topLeft and "X" in topCenter and "X" in topRight:
        print("The winner is player X!")
        break
    elif "X" in middleLeft and "X" in middleCenter and "X" in middleRight:
        print("The winner is player X!")
        break
    elif "X" in bottomLeft and "X" in bottomCenter and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topLeft and "X" in middleLeft and "X" in bottomLeft:
        print("The winner is player X!")
        break
    elif "X" in topCenter and "X" in middleCenter and "X" in bottomCenter:
        print("The winner is player X!")
        break
    elif "X" in topRight and "X" in middleRight and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topLeft and "X" in middleCenter and "X" in bottomRight:
        print("The winner is player X!")
        break
    elif "X" in topRight and "X" in middleCenter and "X" in bottomLeft:
        print("The winner is player X!")
        break
    else:
        print("The game is a tie!")
        break

# This statement prevents the application from exiting when a victory or a time is called.
input("\n\nPress enter to exit the application.")
