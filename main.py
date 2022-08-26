# Example 1 to do power by using function
def raise_to_power(base_num , pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3 , 3))

# Example 2 to do power
print(2**4) #2^4

