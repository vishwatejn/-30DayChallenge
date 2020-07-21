# Middle of Linked_List
def findMid(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
    return slow.data
    '''
    c=0
    x=head
    while head!=None:
        c+=1
        head=head.next    
    c=c//2
    while c>0:
        c=c-1
        x=x.next
    
    return x.data
    ''''
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head))
