import java.util.*;
import java.lang.*;
import java.io.*;

class knap {
    public static int max(int a,int b){
        if(a>=b)
        return a;
        else
        return b;
    }
    public static int knap(int v[],int w[],int total){
        int n=v.length;
        int k[][]=new int[n+1][total+1];
        for(int i=0;i<n+1;i++){
            for(int j=0;j<total+1;j++){
                if(i==0 || j==0){
                    k[i][j]=0;
                }
                else if(w[i-1]<=j){
                    k[i][j]=max(v[i-1]+k[i-1][j-w[i-1]],k[i-1][j]);
                }
                else{
                    k[i][j]=k[i-1][j];
                }
            }
        }
        // for(int i=0;i<n+1;i++){
        //     for(int j=0;j<total+1;j++){
        //         System.out.print(k[i][j]+" ");
        //     }
        //     System.out.println();
        // }
        return k[n][total];
    }
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
        int cases=sc.nextInt();
        for(int c=0;c<cases;c++){
            int n=sc.nextInt();
            int total=sc.nextInt();
            int w[]=new int[n];
            int v[]=new int[n];
            for(int i=0;i<n;i++){
                v[i]=sc.nextInt();
            }
            for(int i=0;i<n;i++){
                w[i]=sc.nextInt();
            }
            int ans=knap(v,w,total);
            System.out.println(ans);

        }

	}
}