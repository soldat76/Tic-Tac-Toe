## TicTacToe2.py
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
print("\t\t\t\t|7|  |8|  |9|\n\n\t\t\t\t|4|  |5|  |6|\n\n\t\t\t\t|1|  |2|  |3|")

# This statement tells the users that whoever goes first will be the X's.
print("\n\n\nThe player going first will be the X's. The other player will be the O's")

# Define the variables that determine X or O placement on the board.

# This is the X user input variable that determines placement of X.
def UserXInput():
    global topLeft
    global topCenter
    global topRight
    global middleLeft
    global middleCenter
    global middleRight
    global bottomLeft
    global bottomCenter
    global bottomRight
    
    while True:
        userDecision = input("\nPLAYER X: \nUsing the numbered board as guidance, type in the number to indicate where you want your X: ")
        if "7" in userDecision:
            topLeft = "X"
            break
        elif "8" in userDecision:
            topCenter = "X"
            break
        elif "9" in userDecision:
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
        elif "1" in userDecision:
            bottomLeft = "X"
            break
        elif "2" in userDecision:
            bottomCenter = "X"
            break
        elif "3" in userDecision:
            bottomRight = "X"
            break
        else:
            print("\nInvalid. Try again.")
            
    # This print statement will print out the result.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))
# This is the O user input variable that determines placement of O.
def UserOInput():
    global topLeft
    global topCenter
    global topRight
    global middleLeft
    global middleCenter
    global middleRight
    global bottomLeft
    global bottomCenter
    global bottomRight
    
    while True:
        userDecision = input("\nPLAYER O: \nUsing the numbered board as guidance, type in the number to indicate where you want your O: ")
        if "7" in userDecision and " " in topLeft:
            topLeft = "O"
            break
        elif "8" in userDecision and " " in topCenter:
            topCenter = "O"
            break
        elif "9" in userDecision and " " in topRight:
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
        elif "1" in userDecision and " " in bottomLeft:
            bottomLeft = "O"
            break
        elif "2" in userDecision and " " in bottomCenter:
            bottomCenter = "O"
            break
        elif "3" in userDecision and " " in bottomRight:
            bottomRight = "O"
            break
        else:
            print("\nInvalid. Try again.")

# Results are printed.
    print("\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|\n\n\t\t\t\t|{}|  |{}|  |{}|"
          .format(topLeft,topCenter,topRight,middleLeft,middleCenter,middleRight,bottomLeft,bottomCenter,bottomRight))


# Define a variable that checks win condition for X. If a win is detected, stop the program.
def UserXWin():
    if "X" in topLeft and "X" in topCenter and "X" in topRight:
        return False
    elif "X" in middleLeft and "X" in middleCenter and "X" in middleRight:
        return False
    elif "X" in bottomLeft and "X" in bottomCenter and "X" in bottomRight:
        return False
    elif "X" in topLeft and "X" in middleLeft and "X" in bottomLeft:
        return False
    elif "X" in topCenter and "X" in middleCenter and "X" in bottomCenter:
        return False
    elif "X" in topRight and "X" in middleRight and "X" in bottomRight:
        return False
    elif "X" in topLeft and "X" in middleCenter and "X" in bottomRight:
        return False
    elif "X" in topRight and "X" in middleCenter and "X" in bottomLeft:
        return False
    else:
        return True

# Define a variable that checks win condition for O. If a win is detected, stop the program.
def UserOWin():
    if "O" in topLeft and "O" in topCenter and "O" in topRight:
        return False
    elif "O" in middleLeft and "O" in middleCenter and "O" in middleRight:
        return False
    elif "O" in bottomLeft and "O" in bottomCenter and "O" in bottomRight:
        return False
    elif "O" in topLeft and "O" in middleLeft and "O" in bottomLeft:
        return False
    elif "O" in topCenter and "O" in middleCenter and "O" in bottomCenter:
        return False
    elif "O" in topRight and "O" in middleRight and "O" in bottomRight:
        return False
    elif "O" in topLeft and "O" in middleCenter and "O" in bottomRight:
        return False
    elif "O" in topRight and "O" in middleCenter and "O" in bottomLeft:
        return False
    else:
        return True
    
# Game program starts here

        
# X User input will now start. 
UserXInput()

# O user input will now start.    
UserOInput()

# X user input, 2nd turn.
UserXInput()

# O user input, 2nd turn.
UserOInput()

# X user input, 3rd turn.
UserXInput()

# Start checking the win condition (3 X's or O's in a row)

# Check win condition for X.
if UserXWin() is False:
    print("The winner is player X!")
    
# O user input, 3rd turn.
else:
    UserOInput()
    
# Checking win condition O (3 X's or O's in a row)
if UserXWin() is True:
    if UserOWin() is False:
        print("The winner is player O!")
    
# X user input, 4th turn.
if UserXWin() is True and UserOWin() is True:
    UserXInput()

# Checking win condition X (3 X's or O's in a row)
    if UserXWin() is False:
        print("The winner is player X!")
        
# O user input, 4th turn.
if UserXWin() is True and UserOWin() is True:
    UserOInput()

# Checking win condition O (3 X's or O's in a row)
    if UserOWin() is False:
        print("The winner is player O!")

# X user input, 5th turn.
if UserXWin() is True and UserOWin() is True:
    UserXInput()
                
# Checking win condition X (3 X's or O's in a row)
    if UserXWin() is False:
        print("The winner is player X!")

# Tie statement.
if UserXWin() is True and UserOWin() is True:
    print("The game is a tie!")
        
# This statement prevents the application from exiting when a victory or a time is called.
input("\n\nPress enter to exit the application.")
