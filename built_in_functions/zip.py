names = ("Ayush", "Harsh", "Hrishi", "Ayush", "Ayush")
companies = ("Dell", "Visa", "Amex", "Facebook", "Dell")

zipped = zip(names, companies)

# zip object returned
print('zip(names, companies): ', zipped)

# Order will be maintained
print('\nlist(zipped): ', list(zip(names, companies)))

# Order will not be maintained, because keys are hashed (hashset)
print('\nset(zipped): ', set(zip(names, companies)))

print('\ntuple(zipped): ', tuple(zip(names, companies)))

print('\ndict(zipped): ', dict(zip(names, companies)), "\n")

# Iterable
for zip_val in zipped:
    print('zip_val: ', zip_val)

print("\n")

# enumerate
for idx, zip_val in enumerate(zip(names, companies)):
    print('idx, zip_val: ', idx, zip_val)
