class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        i=0
        j=n
        alt=True
        while j<2*n:
            if alt:
                ans.append(nums[i])
                i+=1
                alt=False
            else:
                ans.append(nums[j])
                j+=1
                alt=True
        return ans         