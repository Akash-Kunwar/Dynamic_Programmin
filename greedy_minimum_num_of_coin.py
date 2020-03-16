coin=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
coin.reverse()
# row=len(coin)
test=int(input())
for _ in range(test):
    total=int(input())
    i=0
    while(total>0 and i<len(coin)):
        if coin[i]<=total:
            print(coin[i],end=' ')
            total-=coin[i]
        else:
            i+=1
    print()
    
    