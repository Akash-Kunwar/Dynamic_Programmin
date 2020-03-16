def longestCommonSubsequence(s1, s2):
    a=[[1]*(len(s2)+1) for i in range(len(s1)+1)]

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if (i==0 or j==0):
                a[i][j]=0
            else:
                if s1[i-1]==s2[j-1]:
                    a[i][j]=a[i-1][j-1]+1
                else:
                    a[i][j]=max(a[i-1][j],a[i][j-1])
    i=len(s1)
    j=len(s2)
    # Following code is used to print LCS 
    index = a[i][j] 
  
    # Create a character array to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = ""
    while(i>0 and j>0):
        if(a[i][j]!=a[i-1][j]):
            lcs[index-1] = s1[i-1] 
            i-=1
            j-=1
            index-=1
        elif a[i-1][j]>a[i][j-1]:
            i=i-1
        else:
            j-=1
    print(" ".join(lcs))
longestCommonSubsequence('398397970','3399917206')

