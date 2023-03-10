# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=1
        end=n
        candi=0
        while start<=end:
            mid=(start+end)//2
            if isBadVersion(mid)==False:
                candi=mid
                start=mid+1
            else:
                end=mid-1
        return candi+1      
        