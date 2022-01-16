with open('input.txt') as x:
    lines = x.readlines()

lines = [x.strip() for x in lines]

move_dict = {
    "forward": "x+",
    "down": "y+",
    "up": "y-"
}
depth = 0
horiz = 0
x = 0
y = 0
aim = 0

for n in lines:
    if move_dict[n[:-2]] == 'x+':
        x = eval(str(move_dict[n[:-2]]) + str(n[-1]))
        horiz = horiz + int(n[-1])
    elif move_dict[n[:-2]] == 'y+':
        aim += 5
    elif move_dict[n[:-2]] == 'y-':
        aim -= 5
    depth = horiz * aim
print(horiz*depth)


