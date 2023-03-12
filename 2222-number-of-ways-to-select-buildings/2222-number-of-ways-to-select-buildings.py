class Solution:
        
    def numberOfWays(self, s: str) -> int:
        d={'0':0,'1':0,'01':0,'10':0,'010':0,'101':0}
        for i in s:
            if i=='0':
                d['0']=d['0']+1
                d['10']+=d['1']
                d['010']+=d['01']
            else:
                d['1']=d['1']+1
                d['01']+=d['0']
                d['101']+=d['10']
        return d['101']+d['010']       
                