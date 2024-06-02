#Changes the character representing the pentomino.
def change_pentomino(original,change):
    for i in range(5):
        for j in range(5):
            if original[i][j] == "x":
                original[i][j] = change
    return original

#Base format of each of the pentominoes.
F = [["•","•","•","•","•"],
     ["•","•","x","x","•"],
     ["•","x","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","•","•","•"]
    ]

I = [["•","•","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"]
    ]

L = [["•","•","•","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","x","•"]
    ]

M = [["•","•","•","•","•"],
     ["•","x","x","•","•"],
     ["•","•","x","x","•"],
     ["•","•","•","x","•"],
     ["•","•","•","•","•"]
    ]

N = [["•","•","•","•","•"],
     ["•","x","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","x","•"],
     ["•","•","•","•","•"]
    ]

P = [["•","•","•","•","•"],
     ["•","•","x","x","•"],
     ["•","•","x","x","•"],
     ["•","•","x","•","•"],
     ["•","•","•","•","•"]
    ]

T = [["•","•","•","•","•"],
     ["•","x","x","x","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"],
     ["•","•","•","•","•"]
    ]

U = [["•","•","•","•","•"],
     ["•","•","•","•","•"],
     ["•","x","•","x","•"],
     ["•","x","x","x","•"],
     ["•","•","•","•","•"]
    ]

V = [["•","•","•","•","•"],
     ["•","x","•","•","•"],
     ["•","x","•","•","•"],
     ["•","x","x","x","•"],
     ["•","•","•","•","•"]
    ]

X = [["•","•","•","•","•"],
     ["•","•","x","•","•"],
     ["•","x","x","x","•"],
     ["•","•","x","•","•"],
     ["•","•","•","•","•"]
    ]

Y = [["•","•","•","•","•"],
     ["•","•","x","•","•"],
     ["•","•","x","x","•"],
     ["•","•","x","•","•"],
     ["•","•","x","•","•"]
    ]

Z = [["•","•","•","•","•"],
     ["•","•","•","•","•"],
     ["•","x","x","•","•"],
     ["•","•","x","x","x"],
     ["•","•","•","•","•"]
    ]
#Asks the user which pentomino they want to print and sets it as the chosen pentomino.
while True:
    answer = input("Pentomino to print(F,I,L,M,N,P,T,U,V,X,Y,Z): ")

    if answer == "F":
        pentomino = F
        break
    elif answer == "I":
        pentomino = I
        break
    elif answer == "L":
        pentomino = L
        break
    elif answer == "M":
        pentomino = M
        break
    elif answer == "N":
        pentomino = N
        break
    elif answer == "P":
        pentomino = P
        break
    elif answer == "T":
        pentomino = T
        break
    elif answer == "U":
        pentomino = U
        break
    elif answer == "V":
        pentomino = V
        break
    elif answer == "X":
        pentomino = X
        break
    elif answer == "Y":
        pentomino = Y
        break
    elif answer == "Z":
        pentomino = Z
        break
    else:
        print("Sorry, that is not a pentomino.")

#Changes the character of the pentomino, using the change_pentomino function and ensuring it is only one character.
while True:
    letter = input("which character would you like to represent the pentomino? ")
    if len(letter) == 1:
        pentomino = change_pentomino(pentomino, letter)
        break
    print("Sorry, that string is not 1 character long. Try again.")

#Asks the user which transformation they want applied to the base pentomino.
while True:
    transformation = input("Transformation(None, Flip, Rotate): ")

    if transformation == "None":
        #Prints the base pentomino.
        for i in range(5):
            print(" ".join(pentomino[i]))
        break
    elif transformation == "Flip":
        #Flips the base pentomino either horizontally or vertically depending on the users input, then prints the new pentomino.
        while True:
            which_flip = input("Flip along vertical or horizontal? ")
            if which_flip == "horizontal":
                for i in range(5):
                    print("")
                    for j in range(5):
                        print(pentomino[i][4-j], end = " ")
                break
            elif which_flip == "vertical":
                for i in range(5):
                    print(" ".join(pentomino[4-i]))
                break
            else:
                print("Sorry that is not a valid direction. Try horizontal or vertical.")
        break
    elif transformation == "Rotate":
        #Rotates the base pentomino either 90, 180 or 270 degrees depending on the users input, then prints the new pentomino.
        while True:
            which_rotation = input("Rotate how many degrees(90, 180, 270)? ")
            if which_rotation == "90":
                for i in range(5):
                    for j in range(5):
                        print(pentomino[4-j][i], end = " ")
                    print("")
                break
            elif which_rotation == "180":
                for i in range(5):
                    print("")
                    for j in range(5):
                        print(pentomino[4-i][4-j], end = " ")
                break
            elif which_rotation == "270":
                for i in range(5):
                    print("")
                    for j in range(5):
                        print(pentomino[j][4-i], end = " ")
                break
            else:
                print("Sorry that is not a valid angle. Try 90, 180 or 270.")
        break
    else:
        print("Sorry, that is not a valid transformation. Try None, Flip or Rotate.")
                    
            







