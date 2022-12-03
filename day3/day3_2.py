# Advent of Code 2022 Day 3
# Part 2

from day3_1 import get_priority

def main():
    file = open("input.txt")
    total = 0
    for line in file:
        first, second, third = line.strip(), next(file).strip(), next(file).strip()
        for item in first:
            if item in second and item in third:
                total += get_priority(item)
                break # start looking at the next three lines
    print(total)

if __name__ == "__main__":
    main()