class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        start=0
        end=len(arr)-1
        candi=0
        while start<=end:
            mid=start+(end-start)//2
            if mid-1>=0 and mid+1<n and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                #print(arr[mid])
                return mid
            elif mid-1<0 or arr[mid]>arr[mid-1]:
                start=mid+1
            else:
                end=mid-1
      
        return mid
                
                
        
        