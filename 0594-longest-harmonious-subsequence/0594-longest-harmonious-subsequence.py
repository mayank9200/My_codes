class Solution:
    #just see how simple the code becomes from the given link below
    def findLHS(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/longest-harmonious-subsequence/discuss/103534/Python-Straightforward-with-Explanation
        count={}
        for i in nums: 
            count[i]=count.get(i,0)+1 #storing the frequency of each number
        maxx=0    
        for i in nums:
            if i+1 in count:
                maxx=max(maxx,count[i]+count[i+1]) #maximum value of all the occurances if i and i+1
        return maxx        