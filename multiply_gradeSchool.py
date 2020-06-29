def multiply(x, y):
    
    # Obtain the lengths of each factor
    _x = len(str(x))
    _y = len(str(y))

    results = []

    # Simulate grade-school multiplication with iterations
    i = 0
    while i < _y:
        y_i = (y // 10**i) % 10 # Obtain multiplier

        carry = 0
        result_str = ""

        j = 0
        while j < _x:
            x_j = (x // 10**j) % 10 # Obtain multiplicand

            # Multiply ... Then split keep and carry from product
            product = x_j * y_i
            product += carry
            keep = (product // 1) % 10
            carry = (product // 10) % 10

            # Pad result string with zeros ... Once for every multiplier 'i' that is > 0
            if i > 0 and j == 0:
                zeros = '0' * i
                result_str = str(keep) + result_str + zeros
            else: 
                result_str = str(keep) + result_str

            # Add leftover carry to last number ... Once for every multiplier 'i'
            if j == _x - 1 and carry > 0:
                result_str = str(carry) + result_str

            j += 1
            
        i += 1

        results.append(result_str)

    # Sum all results
    final = 0
    for value in results:
        final += int(value)

    return final

# Main code
a = 316116264883176053652066592247340373432072078
b = 886360317032616107264749429648073824285408907
result = multiply(a, b)
print('Result: %d' % result)

expected = 280192912761018376885416365905516189158531620076422058864340512961582507471305802527198746
if (result == expected):
    print('Success!')
else:
    print('Expected number and multiplication result do not match')