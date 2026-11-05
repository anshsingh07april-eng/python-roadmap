#Q3. Mutability trap. Before running anything, write your prediction in a comment for each snippet, then run it and compare:
#• a = [1, 2, 3], b = a, b.append(4), print(a)
#• a = [1, 2, 3], b = a[:], b.append(4), print(a)
#• a = [[1, 2], [3, 4]], b = a.copy(), b[0].append(99), print(a)
#• the same as the third, but with copy.deepcopy
#In a comment, explain the difference between assignment, shallow copy and deep copy.

import copy

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Prediction: [1, 2, 3, 4]

a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)  # Prediction: [1, 2, 3]

a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)  # Prediction: [[1, 2, 99], [3, 4]]

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)  # Prediction: [[1, 2], [3, 4]]
