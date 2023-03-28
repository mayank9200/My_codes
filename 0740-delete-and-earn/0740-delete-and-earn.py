class Solution:
    #https://leetcode.com/problems/delete-and-earn/discuss/109871/Awesome-Python-4-liner-with-explanation-Reduce-to-House-Robbers-Question 
    def deleteAndEarn(self, nums: List[int]) -> int:
        #similar to house and robber problem,just calculate gold at every index and we cannot take two consecutive houses, as simple as that
        n=len(nums)
        m=max(nums)
        arr=[0 for i in range(m+1)]
        for i in nums:
            arr[i]+=i
        inc=arr[0]
        exc=0
        for i in range(1,m+1):
            tinc=inc #just store because its value is getting changed
            inc=exc+arr[i]
            exc=max(exc,tinc)
        return max(inc,exc)    