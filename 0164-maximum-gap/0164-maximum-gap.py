class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        if len(nums)==2:
            return nums[1]-nums[0]
        maxx=max(nums)
        minn=min(nums)
        if maxx==minn:
            return 0
        g=ceil((maxx-minn)/(len(nums)-1))
        size_bucket=((maxx-minn)//g) + 1
        buckets=[[] for i in range(size_bucket)]
        for i in buckets:
            i.append(float('inf'))
            i.append(float('-inf'))
            #[1,3],[4,6],[7,9],[10,12]
        for i in nums:
            bucknum=(i-minn)//g
            if i<buckets[bucknum][0]:
                buckets[bucknum][0]=i
            if i>buckets[bucknum][1]:
                buckets[bucknum][1]=i
        nbuckets=[]
        for i in buckets:  
            if i[0]!=float('inf'):
                nbuckets.append(i)
        maxi=float('-inf')
        for i in range(1,len(nbuckets)):
            maxi=max(maxi,nbuckets[i][0]-nbuckets[i-1][1])
        return maxi    
                
        