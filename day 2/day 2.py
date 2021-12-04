with open('input.txt') as x:
    lines = x.readlines()

lines = [x.strip() for x in lines]
print(lines)

move_dict = {
    "forward": "x+",
    "down": "y+",
    "up": "y-"
}

x = 0
y = 0

for n in lines:
    a = move_dict[n[:-2]]
    b = n[-1]

    if a == 'x+':
        x = eval(str(a) + str(b))
    else:
        y = eval(str(a) + str(b))

print(x*y)
