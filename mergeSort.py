def mergeSort(A):

    # Get problem size
    n = len(A)

    if (n == 1):
        return A
    if (n > 1):
        print('pre-merge():', A)
        mid = n // 2

        # Split subproblems
        B = A[:mid]
        C = A[mid:]

        # Recursive calls
        B = mergeSort(B)
        C = mergeSort(C)

        # Sort
        D = [0] * n
        k = 0
        i = 0
        j = 0

        while i < len(B) and j < len(C):
            if B[i] < C[j]:             
                D[k] = B[i]
                i += 1
                k += 1
            elif C[j] < B[i]:
                D[k] = C[j]
                j += 1
                k += 1

        # Include left-over index after sorting
        while i < len(B):
            D[k] = B[i]
            i += 1
            k += 1

        while j < len(C):
            D[k] = C[j]
            j += 1
            k += 1

        print('post-merge():', D)
        return D

# Main code
array = [11, 3, 5, 2, 0]
result = mergeSort(array)

print(result)
