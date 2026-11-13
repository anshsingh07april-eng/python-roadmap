#Q10. Matrix row and column sums. Store a 3 by 3 grid. Print the sum of each row and the sum of each column.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, row in enumerate(matrix):
    print(f"Sum of row {i + 1}: {sum(row)}")

for j in range(len(matrix[0])):
    column_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"Sum of column {j + 1}: {column_sum}")