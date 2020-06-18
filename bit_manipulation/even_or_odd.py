# If last bit enabled, odd else even

def even_or_odd(number : int):
    return "odd" if (number & (1)) else "even"

print('even_or_odd(1): ', even_or_odd(1))
print('even_or_odd(2): ', even_or_odd(2))
print('even_or_odd(3): ', even_or_odd(3))
print('even_or_odd(4): ', even_or_odd(4))