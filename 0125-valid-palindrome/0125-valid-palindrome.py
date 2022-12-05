class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''
        for i in s:
            if ord(i.lower()) in range(97,123):
                ss=ss+i.lower()
            elif ord(i) in range(48,58):
                ss=ss+i
        #print(ss)        
        if ss==ss[::-1]:
            return True
        else:
            return False
        