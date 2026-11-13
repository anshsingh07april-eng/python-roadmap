#Q3. Find the duplicates. Given a list, print every number that appears more than once. Do it with a set called seen: if a number is already in seen, it is a duplicate.
numbers = [4, 7, 4, 9, 7, 1]
seen = set()
duplicates = set()

for n in numbers:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print("Duplicates:", list(duplicates))
