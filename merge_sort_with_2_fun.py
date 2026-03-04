def merge(a,b):
    (C, m, n) = ([], len(a), len(b))
    (i, j) = (0, 0)

    while i+j < m+n:
        if i == m:
            C.append(b[j])
            j=j+1
        elif j == n:
            C.append(a[i])
            i=i+1
        elif a[i] <= b[j]:
            C.append(a[i])
            i=i+1
        elif a[i] > b[j]:
            C.append(b[j])
            j=j+1
    return(C)

