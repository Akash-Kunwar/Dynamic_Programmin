def getWays(n, c):
    a=[[0]*(n+1)]*len(c)
    for i in range(len(c)):
        for j in range(n+1):
            if j==0:
                a[i][j]=1
            elif i==0:
                if j % c[i]==0:
                    a[i][j]=1
                else:
                    a[i][j]=0
            elif c[i]>j:
                a[i][j]=a[i-1][j]
            else:
                a[i][j]=a[i-1][j]+a[i][j-c[i]]
    print(a[-1][-1])
getWays(10,[2,3,5,6])