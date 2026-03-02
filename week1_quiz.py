#def h(n):
 #   s = 0
  #  for i in range(2,n):
   #     if n%i == 0:
   #        s = s+i
    #return(s)

#print(h(60) - h(45))

def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)

