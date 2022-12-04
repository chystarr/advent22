# Advent of Code 2022 Day 4

def main():
    file = open("input.txt")

    fully_contained = 0
    for line in file:
        assignments = line.strip().split(",")
        first, second = assignments[0].split("-"), assignments[1].split("-")
        first[0], first[1], second[0], second[1] = int(first[0]), int(first[1]), int(second[0]), int(second[1])
       
        # Part 1
        # check if the first range fully includes the second
        #if first[0] <= second[0] and first[1] >= second[1]:
            #fully_contained += 1
        # check if the second range fully includes the first
        #elif second[0] <= first[0] and second[1] >= first[1]:
            #fully_contained += 1
        
        # Part 2
        # check if the first range partially or fully includes the second
        if (first[0] <= second[0] and first[1] >= second[0]) or (first[0] <= second[1] and first[1] >= second[1]):
            fully_contained += 1
        # check if the second range partially or fully includes the first
        elif (second[0] <= first[0] and second[1] >= first[0]) or (second[0] <= first[1] and second[1] >= first[1]):
            fully_contained += 1

    file.close()
    print(fully_contained)

if __name__ == "__main__":
    main()