class Solution:
    # @param A : integer
    # @return a strings
    def gen(a):
        count=1
        s=''
        i=0
        while(i<=len(a)-1):
            if(i==len(a)-1):
                s+=str(count)+str(a[i])
                return s

            if(a[i]==a[i+1]):
                count+=1
            else:
                s+=str(count)+str(a[i])
                count=1
            i+=1
        return s
    def countAndSay(self, A):
        t='1'
        if(A==1):
            print(t)
        else:
            for i in range(1,A):
                s=Solution.gen(t)
                t=s
            print(s)
            
s=Solution()
s.countAndSay(4)