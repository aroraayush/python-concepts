names = ("Ayush", "Harsh", "Hrishi", "Ayush", "Ayush")
companies = ("Dell", "Visa", "Amex", "Facebook", "Dell")

zipped = zip(names, companies)

# zip object returned
print('zip(names, companies): ', zipped)
# zip(names, companies):  <zip object at 0x7fcd022701c0>

# Order will be maintained
print('\nlist(zipped): ', list(zip(names, companies)))
# list(zipped):  [('Ayush', 'Dell'), ('Harsh', 'Visa'), ('Hrishi', 'Amex'), ('Ayush', 'Facebook'), ('Ayush', 'Dell')]

# Order will not be maintained, because keys are hashed (hashset)
print('\nset(zipped): ', set(zip(names, companies)))
# set(zipped):  {('Ayush', 'Facebook'), ('Ayush', 'Dell'), ('Harsh', 'Visa'), ('Hrishi', 'Amex')}

print('\ntuple(zipped): ', tuple(zip(names, companies)))
# tuple(zipped):  (('Ayush', 'Dell'), ('Harsh', 'Visa'), ('Hrishi', 'Amex'), ('Ayush', 'Facebook'), ('Ayush', 'Dell'))

print('\ndict(zipped): ', dict(zip(names, companies)), "\n")
# dict(zipped):  {'Ayush': 'Dell', 'Harsh': 'Visa', 'Hrishi': 'Amex'} 

# Iterable
for zip_val in zipped:
    print('zip_val: ', zip_val)

# zip_val:  ('Ayush', 'Dell')
# zip_val:  ('Harsh', 'Visa')
# zip_val:  ('Hrishi', 'Amex')
# zip_val:  ('Ayush', 'Facebook')
# zip_val:  ('Ayush', 'Dell')
print("\n")

# enumerate
for idx, zip_val in enumerate(zip(names, companies)):
    print('idx, zip_val: ', idx, zip_val)

# idx, zip_val:  0 ('Ayush', 'Dell')
# idx, zip_val:  1 ('Harsh', 'Visa')
# idx, zip_val:  2 ('Hrishi', 'Amex')
# idx, zip_val:  3 ('Ayush', 'Facebook')
# idx, zip_val:  4 ('Ayush', 'Dell')