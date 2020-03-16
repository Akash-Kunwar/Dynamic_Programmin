arr=list(map(int ,input().split()))
n=len(arr)
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if(arr[i]>arr[j]):
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))



# given-> 10 22 9 33 21 50 41 60 890
# Output:6
#longest increasing subsequence is 10 22 33 50 60 890

# Inp:->50 3 10 7 40 80
# out:->4