#Q8. Matrix basics. Store a 3 by 3 matrix as a list of lists. Print it neatly, then print its transpose, the sum of each row, and the sum of both diagonals. Do not use NumPy.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix neatly
print("Original Matrix:")
for row in matrix:
    print(row)

# Print the transpose
print("\nTranspose:")
for row in zip(*matrix):
    print(list(row))

# Print the sum of each row
print("\nSum of each row:")
for i, row in enumerate(matrix):
    print(f"Row {i + 1}: {sum(row)}")

# Print the sum of both diagonals
print("\nSum of both diagonals:")
primary_diagonal = sum(matrix[i][i] for i in range(3))
secondary_diagonal = sum(matrix[i][2 - i] for i in range(3))
print(f"Primary diagonal: {primary_diagonal}")
print(f"Secondary diagonal: {secondary_diagonal}")