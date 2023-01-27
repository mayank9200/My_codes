class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Heap technique
        # from heapq import heappush,heappop
        # h=[]
        # ans=[]
        # n=len(arr)
        # for i in range(n):
        #     heappush(h,[abs(arr[i]-x),i])
        # while len(h)>0 and k>0:
        #     k=k-1
        #     temp=heappop(h)
        #     ans.append(arr[temp[1]])
        # ans.sort()
        # return ans
        
        #Binary search + two pointer
        n=len(arr)
        ans=[]
        low=0
        high=n-1
        mid=0
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                break
            elif x<arr[mid]:
                high=mid-1
            else:
                low=mid+1 
        
        if mid==0:
            low=0
            high=1
        else:
            low=mid-1
            high=mid
        while low >=0 and high<n and len(ans)<k:
     
            if abs(arr[low]-x)==abs(arr[high]-x):
                ans.append(arr[low])
                low-=1
            elif abs(arr[low]-x)<abs(arr[high]-x):
                ans.append(arr[low])
                low-=1
            else:
                ans.append(arr[high])
                high+=1   
        while low>=0 and len(ans)<k:
           
            ans.append(arr[low])
            low-=1
        while high<n and len(ans)<k:
       
            ans.append(arr[high])
            high+=1    
        ans.sort()
        return ans        
            