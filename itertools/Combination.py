from itertools import combinations, combinations_with_replacement

letters = ['a', 'b', 'c']

print("\n===== C(n,n) = C(n,1) ===== 'n' = required  ==============")
y = list(combinations(letters,3))

for idx, i in enumerate(y):
    print('combination : ', i)

print("\n====== C(n,k)  ===== 'k' = required ==========")
y2 = list(combinations(letters, 2))

for idx, i in enumerate(y2):
    print('combination : ', i)

print("\n====== Combination with Replacement - Sample duplicate element twice ==========")
y3 = list(combinations_with_replacement(letters, 2))

for idx, i in enumerate(y3):
    print('combination_with_replacement : ', i)

print("\n\n")

letters2 = ['a', 'b', 'c', 'a']
y4 = list(combinations_with_replacement(letters2, 2))

for idx, i in enumerate(y4):
    print('combination_with_replacement ("a" twice) : ', i)