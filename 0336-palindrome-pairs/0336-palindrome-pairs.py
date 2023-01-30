class Solution:
    def ispalin(self,s):
        if s==s[::-1]:
            return True
        return False
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n=len(words)
        ans=[]
        d={}
        for i in range(n):
            d[words[i]]=i   
        # for i in range(n):
        #     if words[i][::-1] in d:
        #         if i!=d[words[i][::-1]]:
        #             ans.append([i,d[words[i][::-1]]])
        for i in words:
            for j in range(len(i)):
                fhalf=i[:j+1]
                shalf=i[j+1:]
                if self.ispalin(fhalf) and shalf[::-1] in d:
                    ans.append([d[shalf[::-1]],d[i]])
                if self.ispalin(shalf) and fhalf[::-1] in d:
                    ans.append([d[i],d[fhalf[::-1]]])
        

        if '' in d:
            for i in range(n):
                if words[i]!='' and words[i][::-1]==words[i]:
                    ans.append([d[words[i]],d['']]) 
        i=0
        while i<len(ans):
            if int(ans[i][0])==int(ans[i][1]):
                print(ans[i])
                ans.remove(ans[i])   
            else:    
                i+=1    
        ans.sort()
        return ans            
                                 
        