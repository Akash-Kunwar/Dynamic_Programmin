def fun(n,a):
    if n==1:
        a[1]=2
    elif n==2:
        a[2]=3
    elif a[n]==-1:
        a[n]=fun(n-1,a) +fun(n-2,a)
    return a[n]
tc=int(input())
for i in range(tc):
    n=int(input())
    a=[-1]*(n+1)
    print(fun(n,a))
