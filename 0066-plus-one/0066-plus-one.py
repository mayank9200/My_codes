class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        last=len(digits)-1
        for i in range(len(digits)-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits[::-1]
            digits[i]=0
            #print(digits)
        if digits[last]==9:
            #print(digits)
            digits[last]=0
            digits.append(1)
            return digits[::-1]
        else:
            digits[last]+=1
            return digits[::-1]
        
        