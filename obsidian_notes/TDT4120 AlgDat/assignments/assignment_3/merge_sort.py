def merge(A, p, q, r):
    # Skriv din kode her
    n_L = q - p + 1
    n_R = r - q 
    L = [0] * n_L
    R = [0] * n_R

    
    for i in range(n_L):
        L[i] = A[p + i]
    for j in range(n_R):
        R[j] = A[q + j + 1]

    i = 0
    j = 0
    k = p 
    
    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < n_L:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n_R:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    # Skriv din kode her
    if p >= r:
        return
    q = p + (r - p) // 2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

  

A = [8, 7, 2, 5, 6, 1, 3, 4, 9, 10, 11, 31, 13, 42]

merge_sort(A, 0, len(A)-1)

print("Ferdig sorted:")
print(A)
