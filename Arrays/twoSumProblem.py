# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A, target))
target = 20
print(two_sum_brute_force(A, target))


# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(array, total):
    ht = []
    for i in range(len(array)):
        if array[i] in ht:
            second_num = total - array[i]
            print("%i and %i" % (array[i], second_num))
            return True
        else:
            ht.append(total - array[i])
    return False


A = [-2, 1, 2, 4, 7, 10]
target = 12

print(two_sum_hash_table(A, target))


# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(array, total):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] + array[j] == total:
            print(array[i], array[j])
            return True

        elif array[i] + array[j] < total:
            i += 1
        else:
            j -= 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A, target))
