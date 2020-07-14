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

print('\ndict(zipped): ', dict(zip(names, companies)))
