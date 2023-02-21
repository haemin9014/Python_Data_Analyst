students_score = [78, 65, 89, 86, 55, 91, 64,  89];

highest = 0;

for scores in students_score:
    if highest < int(scores):
        highest = int(scores);

print(f"highest score is {highest}");