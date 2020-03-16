a=[1,2,3,-1,-9,5,2,-4]
max_so_far=a[0]
max_end_here=0
start=0
end=0
s=0
for i in range(len(a)):
    max_end_here=max_end_here+a[i]
    if(max_so_far<max_end_here):
        max_so_far=max_end_here
        start=s
        end=i
    if(max_end_here<0):
        max_end_here=0
        s=i+1
print(max_so_far,start,end)