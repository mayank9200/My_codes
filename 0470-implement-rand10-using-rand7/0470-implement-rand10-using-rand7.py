# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        a=rand7()
        b=rand7()
        v=(a-1)*7+b
        if v>40:
            return self.rand10()
        else:
            return (v%10)+1
        
        """
        :rtype: int
        """
        