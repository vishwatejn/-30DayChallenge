# Reverse a Linked_List
def reverseList(self):
    # Code here
    pre=None
    cur=self.head
    while cur is not None:
        nex=cur.next
        cur.next=pre
        pre=cur
        cur=nex
    self.head=pre

class node:
    def __init__(self, val):
        self.data = val
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reverse_List = reverseList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reverse_List()
        lis.printList()
