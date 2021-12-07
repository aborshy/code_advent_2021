with open('input.txt') as x:
    lines = x.readlines()

depths = [int(x) for x in lines]
count = 0

for n, x in enumerate(depths):
    for a in range(0,2):
        rolling_total=x[n] + x[n+1] + x[n+2]
        count += 1

print(count)
