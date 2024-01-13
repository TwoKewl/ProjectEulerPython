import sys
sys.set_int_max_str_digits(30000000)

n = 28433 * 2**7830457 + 1
print(n % 10000000000)