# Converts class functions to class properties

class Students:
    def __init__(self, *grades):
        self.grades = grades
        # self.grades:  ([100, 99, 98, 99.5],)
        # *self.grades:  [100, 99, 98, 99.5]
    
    @property
    def total(self):
        print("=== Calculating sum ===")
        return sum(*self.grades)
    
    @property
    def average(self):
        print("=== Calculating average ===")
        return self.total/len(*self.grades)

students = Students([100,99,98,99.5])
print('students.total: ', students.total)
print('students.average: ', students.average)