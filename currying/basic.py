# Currying is the technique of translating the evalution
# of a function that takes multiple arguments into evaluating a
# sequence of function

# f(x, y, z) -> f(x)(y)(z)
# Can be used for Map, Reduce/Fold, max(), min(), sorted()

# f(x, y) = (x*x*x) + (y*y*y)
# h(x) = (x*x*x)
# h(y) = (y*y*y)
# h(x)(y) = h(x)+h(y)
# f(x, y) = h(x)(y)
# Curry f = h(x)(y)

# Currying in Python - Many to Single Argument 
def change(a): 
    def w(b): 
        def x(c): 
            def y(d): 
                def z(e): 
                    print(a, b, c, d, e) 
                return z 
            return y 
        return x 
    return w 
   
print('change(10)(20)(30)(40)(50): ', change(10)(20)(30)(40)(50))

print("=======================================================")

# Change kilometer to meter, meter to centimeter, centimeter to millimeter
def kilometer2millimeter(b, c, d): 
    def a(x): 
        return b(c(d(x))) 
    return a 
      
def kilometer2centimeter(b, c): 
    def a(x): 
        return b(c(x))
    return a 
      
def kilometer2meter(dist):  
    """ Function that converts km to m. """
    return dist * 1000
      
def meter2centimeter(dist):  
    """ Function that converts m to cm. """
    return dist * 100
      
def centimeter2millimeter(dist): 
    """ Function that converts cm to ft. """
    return dist * 10
      
km_mm_val = kilometer2millimeter(kilometer2meter,meter2centimeter,centimeter2millimeter) 
km_cm_val = kilometer2centimeter(kilometer2meter,meter2centimeter) 
print("kilometer2millimeter",km_mm_val(565)) 
print("kilometer2centimeter",km_cm_val(565))

print("=======================================================")
def f(x,y):
    return x + y

def h(x):
    def curried(y):
        return f(x,y)
    return curried

step_h = h(30)(50)
print('step_h: ', step_h)

assert step_h == f(30,50)
print('step_h == f(30,50): ', step_h == f(30,50))

fix_10_in_h = h(10)
for y in range(10):
    print(f'fix_10_in_h({y}) [10 + {y}] = {fix_10_in_h(y)}')