#User function Template for python3
class Solution:
    def hpartition(self,arr,left,right):
        pivot=arr[left]
        while True:
            while arr[left]<pivot:
                left+=1
            while arr[right]>pivot:
                right-=1
            if left>=right:
                return left
            arr[left],arr[right]=arr[right],arr[left]
        return left    
            
    def quicksort(self,arr,left,right):
        if right>left:
            parti=self.hpartition(arr,left,right)
            self.quicksort(arr,left,parti)
            self.quicksort(arr,parti+1,right)
            
            

	def matchPairs(self,nuts, bolts, n):
	    self.quicksort(nuts,0,len(nuts)-1)
        self.quicksort(bolts,0,len(nuts)-1)
	    return 
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends