class Solution:
    def mergesort(self,arr,left,mid,right,count):
        i=left
        j=mid+1
        temp=[]
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=right:
            temp.append(arr[j])
            j+=1
        j=mid+1    
        for i in range(left,mid+1):
            while j<=right and arr[i]>2*arr[j]:
                j+=1
            count[0]+=(j-(mid+1)) 
        i=left
        for k in range(len(temp)):
            arr[i]=temp[k]
            i+=1

            
    def merge(self,nums,left,right,count):
        if right>left:
            mid=left+(right-left)//2
            self.merge(nums,left,mid,count)
            self.merge(nums,mid+1,right,count)
            self.mergesort(nums,left,mid,right,count)
    def reversePairs(self, nums: List[int]) -> int:
        count=[0]
        self.merge(nums,0,len(nums)-1,count)
        return count[0]
    
        
        