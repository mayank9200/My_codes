class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        maxx=0
        countz=0
        # while j<n:
        #     while j<n and countz<=1:
        #         if nums[j]==0:
        #             countz+=1
        #         maxx=max(maxx,j-i)
        #         print(nums[i:j+1])
        #         j+=1
        #     print('sep')    
        #     while i<j and countz>1:
        #         if nums[i]==0:
        #             countz-=1
        #         i+=1
        # return maxx  
        while j<n:
            if nums[j]==0:
                countz+=1
            if countz>1:
                while countz>1:
                    if nums[i]==0:
                        countz-=1
                        i+=1
                    else:
                        i+=1
            maxx=max(maxx,j-i)
            j+=1
        return maxx     
            
                