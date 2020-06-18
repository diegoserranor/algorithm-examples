def karatsuba(x, y):
    
    # Obtain the lengths of each factor
    _x = len(str(x))
    _y = len(str(y))

    # Base case ... single digit factors
    if _x == 1 and _y == 1:
        return x*y

    # Obtain components of sub-problems
    n = max(_x, _y)
    mid = int(n/2)

    a = (x // 10**mid)
    b = (x % 10**mid)

    c = (y // 10**mid)
    d = (y % 10**mid)

    # Recursive calls
    r1 = karatsuba(a,c)
    r2 = karatsuba(b,d)
    r3 = karatsuba(a + b, c + d) - r1 - r2

    result = r1*(10**(mid*2)) + r3*(10**mid) + r2
    return result

# Main code
a = 397251780884885743417556157076659441535537705854738
b = 368197781380686668989630591889574068286726725854738
result = karatsuba(a, b)
print(result)

expected = 146267224371341604380145293747142703488187931770159945367549010817580220853948134987128780099917048644
if (result == expected):
    print('Success!')
else: 
    print('Expected number and karatsuba result do not match')