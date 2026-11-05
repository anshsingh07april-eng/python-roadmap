#Q8. Simple grade. Ask for marks out of 100 and print the grade: 90 and above is A, 75 and above is B, 50 and above is C, below 50 is Fail.
marks = int(input("Enter marks out of 100: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")    