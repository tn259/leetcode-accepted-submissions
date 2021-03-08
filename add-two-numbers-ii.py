# Modify input lists solution
# reverse both lists
# then add each column and carry addition to next column
# could create new list or edit existing
# O(n) T and O(1) space

# if not allowed to edit list
# two stacks for each list
# do the same addition by creating new list with least significant to most 
    significant
# then reverse final list
# O(n) Time O(n) space due to the output list and stacks
# O(n1 + n2)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, l: ListNode) -> ListNode:
        prev = None
        current = l
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
            
    
    def createStack(self, l: ListNode) -> list:
        stack = []
        node = l
        while node != None:
            stack.insert(0, node.val)
            node = node.next
        return stack
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = self.createStack(l1)
        s2 = self.createStack(l2)
        # add the numbers in the two stacks generating a new node each time
        maxStack = s1 if len(s1) > len(s2) else s2
        minStack = s2 if len(s1) > len(s2) else s1
        # fill rest of minStack with 0;s
        while len(maxStack) > len(minStack):
            minStack += [0]
        # create the new list
        head = ListNode(val=0)
        node = head
        for n in maxStack:
            node.val = n
            node.next = ListNode(val=0)
            node = node.next
        # now do the add
        node = head
        carry = False
        for n in minStack:
            if carry:
                node.val += 1
            if n + node.val >= 10:
                node.val = (node.val+n) % 10
                carry = True
            else:
                node.val += n
                carry = False
            node = node.next
        if carry:
            # corner case where we need to prepend the final carry (or append 
                before the reverse):
            node.val = 1
        head = self.reverse(head)
        # remove leading 0's
        while head != None and head.next != None and head.val == 0:
            prev = head
            head = head.next
            prev.next = None
        return head
            
