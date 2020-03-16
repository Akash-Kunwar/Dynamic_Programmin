m=int(input())

a=list(map(int ,input().split()))

d={}

for i in range(len(a)):
    if a[i]% m in d.keys():
        d[a[i]%m]+=1
    else:
        d[a[i]%m]=1

total=0
print(d)
for i in d.keys():
    # if i==0 or i==m/2 and m==even
    if i ==0 or 2*i ==m:
        # print(total)
        total+=(d[i]*d[i]-1)//2

    else:
        if abs(m-i) in d.keys():
            if d[i]>0 and d[abs(m-i)]>0:
                total+=d[i]*d[abs(m-i)]
                d[i]=0
                print(i,abs(m-i))


print(total)


