# Advent of Code 2022 Day 3

# Part 1

def get_priority(item):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if item.islower():
        return ord(item) - 96
    else: # item is uppercase
        return ord(item) - 38

def main():
    file = open("input.txt")
    total = 0
    for line in file:
        rucksack = line.strip()
        first, second = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]
        for item in first:
            if item in second:
                total += get_priority(item)
                break # start looking at the next line
    file.close()
    print(total)

if __name__ == "__main__":
    main()