with open('input.txt') as x:
    lines = x.readlines()

depths = [int(x) for x in lines]
count = 0

# list comp for each sliding pattern
sums = [[depths[n], depths[n+1], depths[n+2]] for n, x in enumerate(depths[:-2])]

# appending last two indexes because i'm lazy
sums.append([depths[-2],depths[-1]])
sums.append([depths[-1]])

# do the thing
for n, x in enumerate(sums):
    if sum(x) > sum(sums[n-1]):
        count += 1

print(count)



