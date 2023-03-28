class Solution:
     #https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83041/JAVA-DP-O(1)-solution.
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #just a combination problem, make blocks fix one digit and see the possiblity of nect pos to be filled
        if n==0: #base case
            return 1
        if n==1: #all 10 numbers
            return 10
        if n==2: # all 10 +_ _(first place can be filled by 9 digits, other can be also by 9)
            return 9*9 +10
        summ=10+9*9 #till 2 we have ans
        val=9*9
        curr=8 #curr val to be multiplied
        for i in range(3,n+1):
            if curr>0:
                val=val*curr
                summ=summ+val
                curr-=1
            else:
                break #since after 8 more blocks, we will have all repeating numbers
        return summ        
            
            
        