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
                inversions += len(B) - i

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
# inputList = [4, 3, 9, 2, 1, 0]
inputList = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
# inputList = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
# inputList = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
(sortedList, result) = inversionCount(inputList)

print('\nTotal Inversions: %d' % result)

resultQuadratic = inversionCount_quadratic(inputList)
if (result == resultQuadratic):
    print('Results match! - Inversions counted correctly')
else:
    print('No match, count from quadratic implementation is: %d' % resultQuadratic)