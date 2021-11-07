cells = list(input("Enter cells: "))
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
