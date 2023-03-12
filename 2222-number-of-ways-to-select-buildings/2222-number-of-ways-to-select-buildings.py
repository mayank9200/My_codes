class Solution:
        
    def numberOfWays(self, s: str) -> int:
        #small steps to reach bigger answer
        #only two subsequences are possible 010 and 101
        d={'0':0,'1':0,'01':0,'10':0,'010':0,'101':0}  
        for i in s:
            if i=='0': #if current is 0
                d['0']=d['0']+1 #freq of 0 will increase by 1
                d['10']+=d['1'] # 0 can be added to all 1 to form 10
                d['010']+=d['01'] #0 can be added to all 01 to form 010
            else:
                d['1']=d['1']+1 #freq of 1 will increase by 1
                d['01']+=d['0'] #1 can be added to all 0 to form 01
                d['101']+=d['10'] #1 can be added to all 10 to form 101
        return d['101']+d['010']  #final count is sum of 010 and 101
                