coin=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
row=len(coin)
test=int(input())
for _ in range(test):
    col=int(input())+1
    dp=[[0]*(col) for i in range(row)]
    for i in range(row):
        for j in range(col):
            if j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=j
            elif coin[i]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-coin[i]])
    
    # print(dp)
    while(i>0 and j>0):
        if(dp[i][j]==dp[i-1][j]):
            i=i-1
        else:
            print(coin[i],end=' ')
            j=j-coin[i]
        if i==0 and j==1:
            print(coin[i])
        

