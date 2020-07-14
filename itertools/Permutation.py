from itertools import permutations

letters = ['a', 'b', 'c']

print("\n============== P(n,n) full length permutation ==============")
y = list(permutations(letters))

for idx, i in enumerate(y):
    print('permutation : ', i)

print("\n====== P(n,k) ===== Restricting to return length 'k' ==========")
y2 = list(permutations(letters, 2))

for idx, i in enumerate(y2):
    print('permutation : ', i)