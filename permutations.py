from itertools import permutations

# Set the value of n (you can change this number as needed)
n = 3

# Generate all permutations of numbers from 1 to n
numbers = list(range(1, n + 1))
all_perms = list(permutations(numbers))

# Print the total number of permutations
print(len(all_perms))

# Print each permutation
for perm in all_perms:
    print(' '.join(map(str, perm)))
