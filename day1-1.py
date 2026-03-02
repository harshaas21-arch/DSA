# improvising gcd
def gcd(m,n):

    cf = []
    for i  in range(1, min(m,n)+1):
        if (m&i)==0 and (n%i)==0:
            cf.append(i)

    return(cf[-1])

#no lists

def gcd1(m,n):

    for i in range(1,min(m,n)+1):
        if (m&i)==0 and (n%i)==0:
            mrcf = i
    return(mrcf)

#scanning backwards

def gcd2(m,n):

    i= min(m,n)

    while i> 0:
        if(m%i) == 0 and (n%i) ==0:
            return(i)
        else:
            i=i-1

# euclids algorithm

def gcd4(m,n):

    if m < n:
        (m,n) = (n,m)

    if(m%n) == 0:
        return(n)
    else:
        diff = m-n
        return(gcd(max(n,diff), min(n,diff)))
    
    