class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        arr=[]
        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                arr.append(nums[i]*nums[i])
                i+=1
            else:
                arr.append(nums[j]*nums[j])
                j-=1
        return arr[::-1]