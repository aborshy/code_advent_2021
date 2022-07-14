import statistics

with open("input.txt") as x:
    inputs = [n.strip() for n in x]

raw_crab_locations = [x.split(',') for x in inputs]
crab_locations = [int(x) for x in raw_crab_locations[0]]

med = statistics.median(crab_locations)

fuel_used = [abs(x-med) for x in crab_locations]

print(sum(fuel_used))
