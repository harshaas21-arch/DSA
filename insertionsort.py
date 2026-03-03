def insertionsort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos - 1