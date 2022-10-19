#User function Template for python3

def minSwap (arr, n, k) : 
    count=0
    for i in arr:
        if i<=k:
            count+=1
    minn=float('inf')        
    greaterk=0
    for i in range(count):
        if arr[i]>k:
            greaterk+=1
    minn=min(minn,greaterk)
    i=0
    j=count
    while j<n:
        if arr[j]>k:
            greaterk+=1
        if arr[i]>k:
            greaterk-=1
        i+=1
        j+=1
        minn=min(minn,greaterk)    
    return minn        
        
        
    
    
    #Complete the function
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends