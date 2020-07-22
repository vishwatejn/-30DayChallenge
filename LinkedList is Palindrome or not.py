# LinkedList is Palindrome or not
import sys
import io
import atexit


def isPalindrome(head):
    s = ""
    while head != None:
        s += str(head.data)
        head = head.next
    if s == s[::-1]:
        return True
    return False


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


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


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
