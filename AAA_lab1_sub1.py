grid = input("Enter Grid input: ")

dir = input("direction (all caps): ")

hash = grid.find("#")

if len(grid) != 9:

    print("Invalid input")

gList = list(grid)


if dir == "LEFT":

    if (hash == 0 or hash == 3 or hash == 6):
        print("Invalid move")
    else:

        i = gList[hash - 1]

        gList[hash - 1] = "#"
        gList[hash] = i


elif dir == "RIGHT":

    if (hash == 2 or hash == 5 or hash == 8):
        print("Invalid move")
    
    else:

        i = gList[hash + 1]

        gList[hash + 1] = "#"
        gList[hash] = i

elif dir == "UP":

    if (hash == 0 or hash == 1 or hash == 2):
        print("Invalid move")
    
    else:
        
        i = gList[hash - 3]

        gList[hash - 3] = "#"
        gList[hash] = i

elif dir == "DOWN":

    if (hash == 6 or hash == 7 or hash == 8):
        print("Invalid move")
    
    else:

        i = gList[hash + 3]

        gList[hash + 3] = "#"
        gList[hash] = i


print("".join(gList))
