"""

"""





# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        
        result = "["
        
        itr = self
        while itr:
            result += str(itr.val) + "->"
            itr=itr.next
    
        return result[:-2] + "]" 

class Solution(object):
    def removeNthFromEnd(self, head, irem):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i=0
        itr = head
        while itr:
            itr=itr.next
            i+=1
        
        # nothing to remove when the index > len
        if head is None or irem > i:
            return head
        
        # remove head
        if irem == i:
            return head.next
        
        # j is the index of the node before the node to be removed
        j=0
        itr = head
        while j < i - irem - 1:
            itr=itr.next
            j+=1
            
        itr.next = itr.next.next
        
        return head
    
    
    
def main():
    
    head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
    
    solution = Solution()
    head = solution.removeNthFromEnd(head, 1)
    
    print(head)
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    