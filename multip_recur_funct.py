# Skyler Kuhn
# This function multiplies two number using recursion.
# Parameters must be two positive integers.

def multiply_recur(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    # if a > 700:
    #    return 'R.I.P Computer, just use a calculator!'
    if a > 1:
        return multiply_recur(a-1, b) + b
a = multiply_recur(2, 3)
print(a)


