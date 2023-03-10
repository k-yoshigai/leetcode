#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#


# @lc code=start


class Node:
    def __init__(self, val: int = None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1 or index < 0:
            return -1

        count = 0
        cur = self.head
        while cur is not None:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        head = self.head
        node = Node(val=val, next=head)
        if head is None:
            self.head = node
            self.length += 1
            return

        head.prev = node
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val=val)
        head = self.head
        if head is None:
            self.head = node
            self.length += 1
            return

        cur = head
        # Find the last node.
        while cur.next is not None:
            cur = cur.next

        node.prev = cur
        cur.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        count = 1
        prev = self.head

        while prev is not None:
            if count == index:
                added_node = Node(val=val, prev=prev)

                if prev.next is not None:
                    added_node.next = prev.next
                    added_node.next.prev = added_node

                prev.next = added_node
                self.length += 1
                return
            prev = prev.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            self.length -= 1
            return

        count = 1
        cur = self.head.next
        while cur is not None:
            if index == count:
                if cur.next is None:
                    cur.prev.next = None
                    cur = None
                else:
                    cur.prev.next, cur.next.prev = cur.next, cur.prev
                self.length -= 1
                return
            cur = cur.next
            count += 1

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    # Your MyLinkedList object will be instantiated and called as such:
    # obj = MyLinkedList()
    # param_1 = obj.get(index)
    # obj.addAtHead(val)
    # obj.addAtTail(val)
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)
    # @lc code=end
