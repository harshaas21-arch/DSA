from merge_sort_with_2_fun import *

def mergesort(a, left, right):
    if right - left <= 1:
        return(a[left:right])
    if right - left > 1:
        mid = (left+right) // 2
        L= mergesort(a, left, mid)
        R= mergesort(a, mid, right)

        return(merge(L,R))