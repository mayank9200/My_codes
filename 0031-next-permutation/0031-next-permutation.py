class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index1=0
        index2=0
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index1=i
                break
        for i in range(n-1,-1,-1):
            if nums[i]>nums[index1]:
                index2=i
                break
        if index1==index2:
            low=0
            high=n-1
            while low<high:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
                high-=1
            return    
        nums[index1],nums[index2]=nums[index2],nums[index1]
        low=index1+1
        high=n-1
        while low<high:
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1
        return     
        """
        Do not return anything, modify nums in-place instead.
        """
        