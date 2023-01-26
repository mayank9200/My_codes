class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # i=0
        # j=0
        # count=0
        # summ=0
        # n=len(nums)
        # while j<n:
        #     summ=summ+nums[j]
        #     if summ<k:
        #         j+=1
        #     elif summ==k:
        #         count+=1
        #         j+=1
        #     else:
        #         while summ>k:
        #             summ=summ-nums[i]
        #             i+=1
        #         if summ==k:
        #             count+=1
        #         j+=1    
        # return count 
        d={}
        count=0
        pre=0
        for i in nums:
            pre=pre+i
            if pre-k in d:
                count+=d[pre-k]
            if pre-k==0:
                count+=1
            d[pre]=d.get(pre,0)+1
        return count
        