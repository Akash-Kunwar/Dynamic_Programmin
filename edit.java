/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class edit {
    public static int min(int a,int b,int c){
        if(a<=b && a<=c)return a;
        else if(b<=a && b<=c) return b;
        else return c;
    }
    // public static int editDist(String str1,String str2,int n,int m){
        
    //     int dp[][]=new int[n+1][m+1];
    //     for(int i=0;i<=n;i++){
    //         for(int j=0;j<=m;j++){
    //             if(i==0)dp[i][j]=j;
    //             else if(j==0)dp[i][j]=i;
    //             else if(str1.charAt(i-1)==str2.charAt(j-1))dp[i][j]=dp[i-1][j-1];
    //             else dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]);
    //         }
    //     }
    //     return dp[n][m];
        
    // }
    public static int editDist(String str1,String str2,int n,int m){
        if(n==0)return m;
        else if(m==0) return n;
        else if(str1.charAt(n-1)==str2.charAt(m-1)) return editDist(str1,str2,n-1,m-1);
        else{
            int remove=editDist(str1,str2,n-1,m);
            int update =editDist(str1,str2,n-1,m-1);
            int insert= editDist(str1,str2,n,m-1);
            return 1+min(remove,update,insert);

        }
    }
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		int test=sc.nextInt();
        sc.nextLine();
		for(int t=0;t<test;t++){
		    String str1=sc.nextLine();
		    String str2=sc.nextLine();
		    int ans=editDist(str1,str2,str1.length(),str2.length());
		    System.out.println(ans);
		}
	}
}