#Q2. Time converter. Take a number of minutes (for example 135) and print it as hours and minutes (2 hours 15 minutes). Use only // and %.
minutes = int(input("Enter the number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{hours} hours {remaining_minutes} minutes")
