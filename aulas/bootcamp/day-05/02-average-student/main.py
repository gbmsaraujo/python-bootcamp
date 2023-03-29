student_heights = input("Input a list of student heghts: ").split()
total_heights = 0
number_of_students = 0

for height in student_heights:
    total_heights += int(height)
    number_of_students += 1

average_heights = round(total_heights/number_of_students)
print(f"Average is: {average_heights}")
