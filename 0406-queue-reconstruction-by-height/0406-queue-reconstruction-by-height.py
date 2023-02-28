class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key=lambda a: [-a[0],a[1]])
        queue = []
        #print(people)
        for p in people:
            queue.insert(p[1], p)
        return queue
        