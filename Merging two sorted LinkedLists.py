# Merging two sorted LinkedLists
def sortedMerge(head_A, head_B):
    temp1=head_A
    temp2=head_B
    temp3=None
    head=None
    if(temp1.data<temp2.data):
        temp3=head=temp1
        temp1=temp1.next
    else:
        temp3=head=temp2
        temp2=temp2.next
    while(temp1!=None and temp2!=None):
        if(temp1.data< temp2.data):
            temp3.next=temp1
            temp1=temp1.next
        else:
            temp3.next=temp2
            temp2=temp2.next
        temp3=temp3.next
    
    if(temp1==None):
        temp3.next=temp2

    elif(temp2==None):
        temp3.next=temp1
    return head

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))