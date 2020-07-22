# Reverse in Groups

def reverse(head, k):
    curr = head
    prev = None
    tail = None
    join = None
    newhead = None
    temp = None
    while curr:
        c = k
        join = curr
        prev = None
        while curr and c > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            c -= 1
        if newhead == None:
            newhead = prev
        if tail != None:
            tail.next = prev
        tail = join
    return newhead


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
