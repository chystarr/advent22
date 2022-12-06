# Advent of Code 2022 Day 5

def main():
    stacks = {
        1: ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
        2: ['S', 'W', 'C'],
        3: ['R', 'Z', 'T', 'M'],
        4: ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
        5: ['G', 'P', 'T', 'L', 'D', 'Z'],
        6: ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
        7: ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
        8: ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
        9: ['Q', 'P', 'D', 'S', 'V']
    }

    file = open("input.txt")
    for line in file:
        words = line.strip().split()
        amount, source, target = int(words[1]), int(words[3]), int(words[5])
        # Part 1
        # for i in range(amount):
            # crate = stacks[source].pop()
            # stacks[target].append(crate)
        
        # Part 2
        crates = stacks[source][len(stacks[source])-amount:]
        del stacks[source][len(stacks[source])-amount:]
        stacks[target].extend(crates)
        
    file.close()

    arrangement = ''
    for i in range(1, 10):
        arrangement += stacks[i][len(stacks[i]) - 1]
    print(arrangement)

if __name__ == "__main__":
    main()