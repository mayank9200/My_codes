#User function Template for python3
class Solution:
    def hpartition(self,arr, low, high):
        pivot = arr[low]
        i = low 
        j = high 
        while True:
            while arr[i] < pivot:
                i += 1
    
            while arr[j] > pivot:
                j -= 1
    
            if i >= j:
                return j
    
            arr[i], arr[j] = arr[j], arr[i]   
            
    def quicksort(self,arr,left,right):
        if right>left:
            parti=self.hpartition(arr,left,right)
            self.quicksort(arr,left,parti)
            self.quicksort(arr,parti+1,right)
            
            

	def matchPairs(self,nuts, bolts, n):
	    self.quicksort(nuts,0,len(nuts)-1)
	    self.quicksort(bolts,0,len(nuts)-1)
	    #print(nuts[0]>nuts[1])
	    return nuts
	    
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