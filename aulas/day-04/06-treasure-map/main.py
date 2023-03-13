row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

line_position = int(position[0]) - 1
col_position = int(position[1]) - 1

map[line_position][col_position] = "X"

print(f"{row1}\n{row2}\n{row3}")
