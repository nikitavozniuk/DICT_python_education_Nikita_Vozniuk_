cells = list(input("Enter cells: "))
count = 0

X = cells.count("X")
O = cells.count("O")
cells_ = cells.count("_")

print("---------")
print("| ", end="")
for item in cells[:3]:
    print(item, end=" ")
print("|")
print("| ", end="")
for item in cells[3:6]:
    print(item, end=" ")
print("|")
print("| ", end="")
for item in cells[6:9]:
    print(item, end=" ")
print("|")
print("---------")


def checkBoard():
    global count
    if cells[0] == cells[4] == cells[8] != "_":
        count += 1
    if cells[2] == cells[5] == cells[8] != "_":
        count += 1
    if cells[1] == cells[4] == cells[7] != "_":
        count += 1
    if cells[2] == cells[4] == cells[6] != "_":
        count += 1
    if cells[0] == cells[3] == cells[6] != "_":
        count += 1
    if cells[6] == cells[7] == cells[8] != "_":
        count += 1
    if cells[0] == cells[1] == cells[2] != "_":
        count += 1
    if cells[3] == cells[4] == cells[5] != "_":
        count += 1


checkBoard()


if count == 0 or count == 1:
    if X == O + 1 or X == O - 1 or X == O:
        if cells[0] == cells[1] == cells[2] != "_":
            print(cells[0] + " wins")
        elif cells[3] == cells[4] == cells[5] != "_":
            print(cells[3] + " wins")
        elif cells[6] == cells[7] == cells[8] != "_":
            print(cells[6] + " wins")
        elif cells[0] == cells[4] == cells[8] != "_":
            print(cells[0] + " wins")
        elif cells[2] == cells[4] == cells[6] != "_":
            print(cells[2] + " wins")
        elif cells[1] == cells[4] == cells[7] != "_":
            print(cells[4] + " wins")
        elif cells[2] == cells[5] == cells[8] != "_":
            print(cells[5] + " wins")
        elif cells[0] == cells[3] == cells[6] != "_":
            print(cells[3] + " wins")
        elif cells_ > 0:
            print("You don't finish game!")
        else:
            print("Draw!")
    else:
        print("Impossible!")
else:
    print("Impossible!")
