class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda a: [-a[0],a[1]]) #first based on height then on k
        queue = []
        #print(people)
        #next step is just like insertion sort
        for p in people:
            queue.insert(p[1], p)
        return queue
        