# Using Two pointers approach

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

# Using Arrays

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list1 = []
        while curr:
            list1.append(curr)
            curr = curr.next

        index = len(list1) - n

        if index == 0:
            return head.next

        prev = list1[index-1]
        prev.next = list1[index].next

        return head      

        

        
                
