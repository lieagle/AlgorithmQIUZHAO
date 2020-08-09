#2相加，如果相加大于10，把除以10的余数放在当前位置，向前一位进位。
#divmod(a,b)等价于返回[a // b, a % b] a除以b的商和余数

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next





#另一种解法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            cur = val + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if cur >= 10:
                val = 1
                cur = cur - 10
            else: 
                val = 0
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next




#ergou的解法和测试用例
# Definition for singly-linked list.
# 9: 55
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}, {str(self.next)})"
    def __repr(self):
        return str(self)
    def __eq__(self, other):
        return str(self)==str(other)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addNode(l1,l2):
            headNode = currentNode = ListNode(0, None)
            c = 0
            while l1 and l2:
                nextNode = ListNode(0, None)
                currentNode.next = nextNode
                sum = l1.val+l2.val + c
                if sum>=10:
                    nextNode.val = sum-10
                    c = 1
                else:
                    nextNode.val = sum
                    c = 0

                l1 = l1.next
                l2 = l2.next
                currentNode = nextNode
            if l1 is None and l2 is None:
                if c==1:
                    currentNode.next = ListNode(1, None)
            elif l1 is None:
                currentNode.next = addNode(l2, ListNode(c,None))
            elif l2 is None:
                currentNode.next = addNode(l1, ListNode(c,None))
            else:
                raise ValueError
            return headNode.next
        return addNode(l1,l2)
    def test(self):
        def createLinkList(lst):
            if not lst:
                return None
            return ListNode(lst[0], createLinkList(lst[1:]))
        print(self.addTwoNumbers(createLinkList([2,4,3]),createLinkList([5,6,4])))
        assert self.addTwoNumbers(createLinkList([2,4,3]),createLinkList([5,6,4]))\
            == createLinkList([7,0,8])
        print(self.addTwoNumbers(createLinkList([2,4,6]),createLinkList([5,6,4])))
        assert self.addTwoNumbers(createLinkList([2,4,6]),createLinkList([5,6,4]))\
            == createLinkList([7,0,1,1])

        print(self.addTwoNumbers(createLinkList([1]),createLinkList([9,9,9])))
        assert self.addTwoNumbers(createLinkList([1]),createLinkList([9,9,9]))\
            == createLinkList([0,0,0,1])

s = Solution()
s.test()



#yigou的解法和测试用例
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next

def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print('')

if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
    
    
    
    