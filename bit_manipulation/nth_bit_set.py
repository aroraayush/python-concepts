# Prgoram to check whether nth bit set or not

# Masking with nth bit
def check_if_nth_bit_set(decimal : int, index: int):
    binary = bin(decimal)       # We will directly work on decimal value
    mask = 1 << index
    bitwise_and = decimal & mask
    print('bitwise_and: ', bitwise_and, end ='')
    if(bitwise_and):
        return True
    return False

# 6 - 0b110  <class 'str'>
print('\t check_if_nth_bit_set(6,0): ', check_if_nth_bit_set(6,0))   #false
print('\t check_if_nth_bit_set(6,1): ', check_if_nth_bit_set(6,1))   #true
print('\t check_if_nth_bit_set(6,2): ', check_if_nth_bit_set(6,2))   #true
print('\t check_if_nth_bit_set(6,3): ', check_if_nth_bit_set(6,3))   #false

print("===================== 1 line Solution =====================")
def check_if_nth_bit_set_1_line(decimal : int, index: int):
    return True if decimal & (1 << index) else False

print('check_if_nth_bit_set_1_line(6,0): ', check_if_nth_bit_set_1_line(6,0))
print('check_if_nth_bit_set_1_line(6,1): ', check_if_nth_bit_set_1_line(6,1))
print('check_if_nth_bit_set_1_line(6,2): ', check_if_nth_bit_set_1_line(6,2))
print('check_if_nth_bit_set_1_line(6,3): ', check_if_nth_bit_set_1_line(6,3))

