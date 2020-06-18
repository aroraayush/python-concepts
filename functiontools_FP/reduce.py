from functools import reduce

# Rolling Computation
marks = [10,9,9.5,9,10]

# Syntax
# reduce(fun,seq)

max_score = reduce(lambda x,y: x if x > y else y,marks)
print('max_score: ', max_score)


students = [
    {"name" : "Ayush", "marks" : 98},
    {"name" : "Akaash", "marks" : 99},
    {"name" : "Anmol", "marks" : 97},
]

sum = reduce(lambda x,y: x + y["marks"], students, 0)
print('sum: ', sum)