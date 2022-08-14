# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        print(l1.next,l2.next)

l1 = [2,4,3]
l2 = [5,6,4]
s = Solution()
s.addTwoNumbers(l1,l2)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total%10)
            remainder = total//10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            curr = curr.next

        if remainder : curr.next = ListNode(remainder)
        return result.next