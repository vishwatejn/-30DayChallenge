# Detecting loop in a LinkedList
def detectLoop(head):
    # code here
    sp = head
    fp = head
    while sp and fp and fp.next:
        sp = sp.next
        fp = fp.next.next
        if sp == fp:
            return True
    return False
    '''
    s=set()
    while head:
        if head in s:
            return True
        s.add(head)
        head=head.next
    return False
    '''
    '''
    while head!=None:
        if head.data<0:
            return True
        else:
            head.data=-head.data
        head=head.next
    return False
    '''


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
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loopHere(int(input()))

        print(detectLoop(LL.head))
