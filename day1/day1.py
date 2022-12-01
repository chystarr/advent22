# Advent of Code 2022 Day 1 Solution

# Part 1

f = open("input.txt")

cal_totals = [0]

for line in f:
    if len(line) == 1:
        cal_totals.append(0)
    else:
        cal_totals[len(cal_totals) - 1] += int(line.strip("\n"))

f.close()

print(max(cal_totals))

# Part 2

total = 0

for i in range(3):
    greatest = max(cal_totals)
    total += greatest
    cal_totals.remove(greatest)

print(total)