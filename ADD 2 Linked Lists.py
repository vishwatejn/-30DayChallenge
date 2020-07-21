# ADD 2 Linked Lists
def reverseList(node):
    pre=None
    cur=node
    while cur is not None:
        nex=cur.next
        cur.next=pre
        pre=cur
        cur=nex
    node=pre
    return node
    
def addLists(first, second):
    a=reverseList(first)
    b=reverseList(second)
    c=0
    f1=a
    f2=b
    prev1=None
    prev2=None
    while a!=None and b!=None:
        if a!=None and b!=None:
            x=a.data+b.data+c
            c=0
            if x>=10:
                c=int(str(x)[:1])
            x=x%10
            a.data=x
            b.data=x
            prev1=a
            prev2=b
            a=a.next
            b=b.next
    if a==None and b!=None:
        b.data=(b.data+c)
        c=0
        if b.data>=10:
            c=int(str(b.data)[:1])
        b.data%=10
        while c>0 and b.next!=None:
            b.next.data=b.next.data+c
            c=0
            if b.next.data>=10:
                c=int(str(b.next.data)[:1])
            b.next.data%=10
            prev2=b
            b=b.next
        if c>0 and b.next==None:
            prev2.next.next=Node(c)
        return reverseList(f2) 
    elif b==None and a!=None:
        a.data=a.data+c
        c=0
        if a.data>=10:
            c=int(str(a.data)[:1])
        a.data%=10
        while c>0 and a.next!=None:
            a.next.data=a.next.data+c
            c=0
            if a.next.data>=10:
                c=int(str(a.next.data)[:1])
            a.next.data%=10
            prev1=a
            a=a.next
        if c>0 and a.next==None:
            prev1.next.next=Node(c)
        return reverseList(f1)
    else:
        if c>0:
            prev1.next=Node(c)
        return reverseList(f1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends