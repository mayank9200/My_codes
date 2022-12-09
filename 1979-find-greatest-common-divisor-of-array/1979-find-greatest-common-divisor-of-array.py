class Solution:
    def gcd(a,b):
        if a==0:
            return b
        return gcd(b%a,b)
    def findGCD(self, nums: List[int]) -> int:
        minn=min(nums)
        maxx=max(nums)
        return gcd(minn,maxx)
        