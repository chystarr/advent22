# Advent of Code Day 2

# Part 1

points = {
    # opponent
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
    #player
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3 # scissors

}

f = open("input.txt")

total_score = 0

for line in f:
    score = 0
    opponent, player = line.split()
    # Add points depending on which move the player selected
    score += points[player]
    # Add points depending on the outcome of the round
    # 0 for a loss; 3 for a draw; 6 for a win
    # win
    if (player == "X" and opponent == "C") or points[player] - 1 == points[opponent] :
        score += 6
    # draw
    elif points[player] == points[opponent]:
        score += 3
    total_score += score

f.close()

print(total_score)