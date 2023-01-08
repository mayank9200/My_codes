#User function Template for python3

def search (arr, n, x, k) : 
    i=0
    while i<n:
        if arr[i]==x:
            return i
        else:
            diff=abs(arr[i]-x)
            i=i+max(1,diff//k)
    return -1        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n, k = map(int , input().split())
    arr = list(map(int, input().strip().split()))
    x = int(input())
    ans = search(arr, n, x, k)
    print(ans)




# } Driver Code Ends