students_scores = input("Input a list of students scores: ").split()

high_score = 0

for score in students_scores:
    if int(score) > high_score:
        high_score = int(score)

print(f"The highest score in the class is: {high_score}")
