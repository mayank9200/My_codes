class Solution:
    #https://www.youtube.com/watch?v=VT4bZV24QNo&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=22
    def rob(self, nums: List[int]) -> int:
        #include exclude theorem dp
        inc=nums[0] #including 1st element
        exc=0 #not including first element
        #meaning of dp is inc and exc are maintained such that they follow the criteria and end at that point of nums
        for i in range(1,len(nums)):
            preinc=inc #to store value of inc as it changes
            inc=exc+nums[i] #include this element
            exc=max(preinc,exc) #exclude this element so anw will be max of previous
            
        return max(inc,exc)    #max of both the variabless
        