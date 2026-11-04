#Q8. Report card. Take marks for 5 subjects (each out of 100). Print the total, the percentage, and the grade (90 and above is A, 75 and above is B, 60 and above is C, 40 and above is D, otherwise Fail). If any single subject is below 33, the result is Fail whatever the percentage. Reject marks outside 0 to 100.
subjects = []
for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i+1}: "))
            if 0 <= mark <= 100:
                subjects.append(mark)
                break
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

total = sum(subjects)
percentage = total / 5

if any(mark < 33 for mark in subjects):
    grade = "Fail"
elif percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Total: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")