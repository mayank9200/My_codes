class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        

    def get(self, index: int) -> int:
        i=0
        curr=self.head
        while curr!=None and i<index: #move till that index
            curr=curr.next
            i+=1
        if curr!=None:   
            return curr.val
        else:           #index >length of linked list
            return -1
            
        

    def addAtHead(self, val: int) -> None:
        temp=Node(val)
        temp.next=self.head
        self.head=temp
        return
            
        

    def addAtTail(self, val: int) -> None:
        curr=self.head
        if self.head==None:
            self.addAtHead(val)
            return
        while curr!=None and curr.next!=None: 
            curr=curr.next
        curr.next=Node(val)
        return 
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        if index==0:
            self.addAtHead(val)
            return
        curr=self.head
        while curr!=None and i<index-1: #move till that indexes previous
            curr=curr.next
            i+=1
        if curr==None:
            return 
        if curr.next==None: #insert at end
            curr.next=Node(val)
        else:   # linking
            temp=Node(val)
            temp.next=curr.next
            curr.next=temp
        return 
        
           
            
        

    def deleteAtIndex(self, index: int) -> None:
        i=0
        if index==0:
            self.head=self.head.next
            return
        curr=self.head
        while curr!=None and i<index-1: #move till indexes previous
            curr=curr.next
            i+=1
        if curr==None:
            return 
        if curr.next!=None: 
            curr.next=curr.next.next #unlink
        return  
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)