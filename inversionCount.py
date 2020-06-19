def sortAndCount(A):
    # Inputs: Unsorted list 'A' / Outputs: Sorted list 'A', counted inversions
    # Description: mergeSort() implementation with an inversion counter

    # Get problem size
    n = len(A)

    # Base case
    if (n == 1):

        inversions = 0

        return (A, inversions)

    # Recursive case
    if (n > 1):

        # Split subproblems
        mid = n // 2
        B = A[:mid]
        C = A[mid:]

        # Recursive calls
        (B, x) = sortAndCount(B)
        (C, y) = sortAndCount(C)

        # Inversions counter
        inversions = x + y

        # Sort, merge, and count 'left' or 'right' inversions
        D = [0] * n
        k = 0
        i = 0
        j = 0

        while i < len(B) and j < len(C):
            if B[i] <= C[j]:             
                D[k] = B[i]
                i += 1
                k += 1
            elif C[j] <= B[i]:
                D[k] = C[j]
                j += 1
                k += 1
                inversions += 1

        # Include left-over indexes after sorting
        while i < len(B):
            D[k] = B[i]
            i += 1
            k += 1

        while j < len(C):
            D[k] = C[j]
            j += 1
            k += 1

        return (D, inversions)

def mergeAndCountSplit(B, C):
    # Inputs: Sorted lists 'B' and 'C'
    # Description: List merge implementation with a 'split' inversion counter

    # Merged list size
    n = len(B) + len(C)

    # Split inversions counter
    splits = 0

    # Merge two lists; sorting based on mergeSort
    D = [0] * n
    k = 0
    i = 0
    j = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:             
            D[k] = B[i]
            i += 1
            k += 1
        elif C[j] <= B[i]: 
            D[k] = C[j]
            j += 1
            k += 1

            # Split inversions are counted by ...
            # Calculating the elements left in B if an element is copied from C to D
            splits += len(B) - i

    # Include left-over index after sorting
    while i < len(B):
        D[k] = B[i]
        i += 1
        k += 1

    while j < len(C):
        D[k] = C[j]
        j += 1
        k += 1

    return (D, splits)

def inversionCount(A):
    # Inputs: Unsorted list 'A'
    # Description: List merge implementation with a 'split' inversion counter

    # Get problem size
    n = len(A)

    # Split into subproblems
    mid = n // 2
    B = A[:mid]
    C = A[mid:]

    # Sort and count 'left' (< n/2) and 'right' (> n/2) sides 
    (sortedB, x) = sortAndCount(B)
    (sortedC, y) = sortAndCount(C)
    (D, z) = mergeAndCountSplit(sortedB, sortedC)

    print('Left side inversions: %d' % x)
    print('Right side inversions: %d' % y)
    print('Split inversions %d' % z)
    total = x + y + z

    return (D, total)
  
def inversionCount_quadratic(A): 
  
    # Get problem size
    n = len(A)

    inversions = 0

    # Nested loop to compare arrays in O(n^2) time
    for i in range(n): 
        for j in range(i + 1, n): 
            if (A[i] > A[j]): 
                inversions += 1
  
    return inversions 

# Main code
inputList = [4, 3, 9, 2, 1, 0]
(sortedList, result) = inversionCount(inputList)

print('\nTotal Inversions: %d' % result)

resultQuadratic = inversionCount_quadratic(inputList)
if (result == resultQuadratic):
    print('Results match! - Inversions counted correctly')
else:
    print('No match, count from quadratic implementation is: %d' % resultQuadratic)