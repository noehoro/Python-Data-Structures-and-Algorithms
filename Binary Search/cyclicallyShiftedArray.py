# Iterative

def find(A):
    min = float('inf')
    minIndex = None
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
            minIndex = i
    return minIndex


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low
