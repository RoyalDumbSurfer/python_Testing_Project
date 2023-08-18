row1 = ["😁️", "🤣️", "😉️"]
row2 = ["🤩️", "😭️", "😴️"]
row3 = ["😹", "🤏", "🤑"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[1])
row = int(position[0])
treasure = 'x'
map[column-1][row-1] = treasure


print(f"{row1}\n{row2}\n{row3}")
