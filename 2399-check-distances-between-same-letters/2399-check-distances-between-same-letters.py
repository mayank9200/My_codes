class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={} #dictionary with key as char and position as two values
        n=len(s)
        for i in range(n):
            if s[i] not in d:
                d[s[i]]=[i]
            else:
                d[s[i]].append(i)      
        for i in range(len(distance)):
            val=chr(ord('a')+i)
            if val not in d: 
                continue
            if d[val][1]-d[val][0]-1!=distance[i]:
                return False
        return True        
            