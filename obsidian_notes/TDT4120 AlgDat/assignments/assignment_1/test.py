
def insertion_sort(A, n):
    for i in range(1, n, 1):
        print(f"Running loop {i}")
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            print(A)
            j = j - 1
        print(f"Inserting {key} into slot {j+1}")
        A[j + 1] = key

    return A

print(insertion_sort([4,2,3,1], 4))

