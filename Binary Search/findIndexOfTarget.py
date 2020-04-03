def find(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
        return None


def find_binary(a, target):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] < target:
            low = mid + 1
        elif a[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0 or a[mid - 1] != target:
                return mid
            high = mid - 1


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find_binary(A, target)
print(x)
