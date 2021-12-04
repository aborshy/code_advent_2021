with open('input.txt') as x:
    lines = x.readlines()

lines = [x.strip() for x in lines]

move_dict = {
    "forward": "x+",
    "down": "y+",
    "up": "y-"
}

x = 0
y = 0

for n in lines:
    if move_dict[n[:-2]] == 'x+':
        x = eval(str(move_dict[n[:-2]]) + str(n[-1]))
    else:
        y = eval(str(move_dict[n[:-2]]) + str(n[-1]))

print(x*y)
