class Solution:
    def binary_search(self,arr):
        start=0
        end=len(arr)-1
        temp=-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]<0:
                temp=mid
                end=mid-1       
            else:
                start=mid+1
        if temp==-1:
            return 0 
        else:
            return len(arr)-temp
                
                
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for arr in grid:
            #print(self.binary_search(arr))
            count=count+self.binary_search(arr)
        return count