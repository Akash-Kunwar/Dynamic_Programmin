import java.util.*;
class candies{

    public static int minCost(int arr[],int n){
        int sum[]=new int[n];
        sum[0]=1;
        for ( int i =1 ;i<n;i++){
            if(arr[i]>arr[i-1])sum[i]=sum[i-1]+1;
            else sum[i]=1;
        }
        int prev=sum[n-1];
        int count=prev;
        for ( int i= n-2 ;i>=1;i--){
            if (prev>=sum[i]){
                sum[i]=sum[i-1]+1;
                
            }
            prev=sum[i];
        }
        return sum[0];
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for (int i = 0;i < n;i ++)arr[i]=sc.nextInt();
        int ans = minCost(arr,n);
        System.out.println(ans);



    }
}