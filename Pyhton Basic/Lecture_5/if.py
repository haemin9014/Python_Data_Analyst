tuna = "fish"
if tuna == "fish":
    print("this is a fish")
else:
    print("it is not an fish");

def calculateGrade(students_marks):
    # Write your code here
    result = [];
    for student in range(len(students_marks)):
        avg = 0;       
        total = 0;
        for totalGrade in range(len(students_marks[student])):
            total += students_marks[student][totalGrade];
        avg = total / (len(students_marks[student]));
        if avg >= 90:
            result.append('A+');
        elif avg < 90 and avg >= 80:
            result.append('A');
        elif avg < 80 and avg >= 70:
            result.append('B')
        elif avg < 70 and avg >= 60:
            result.append('C')
        elif avg < 60 and avg >= 50:
            result.append('D')
        else:
            result.append('F');
    return result;