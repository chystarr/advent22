# Advent of Code Day 2
# Part 2

f = open("input.txt")

points = {
    # moves
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
}

total_score = 0

for line in f:
    opponent_move, outcome = line.split()
    score = 0
    match outcome:
        case "Z": # win
            if opponent_move == "C":
                score += points["A"]
            else:
                score += points[opponent_move] + 1
            score += 6
        case "Y": # draw
            score += points[opponent_move]
            score += 3
        case "X": # lose
            if opponent_move == "A":
                score += points["C"]
            else:
                score += points[opponent_move] - 1
    total_score += score

f.close()

print(total_score)