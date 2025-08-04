grid = input("Enter Grid input: ")

hash = grid.find("#")

if hash != 0 and hash != 1 and hash != 2:

    print("UP")


if hash != 6 and hash != 7 and hash != 8:

    print("DOWN")


if hash != 2 and hash != 5 and hash != 8:

    print("RIGHT")

if hash != 0 and hash != 3 and hash != 6:

    print("LEFT")

