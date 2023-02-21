student_heights = [180, 124, 165, 173, 189, 169, 146];
total_sum = 0;
count = 0;
for students in student_heights:
    total_sum += int(students);
    count += 1;

print(f"Total sum is {total_sum}");
print(f"Number of students are {count}");
print(round(total_sum/count, 2));

