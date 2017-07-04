"""

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
                
        try:
        
            slow = head
            fast = head.next
        
            while ( True ):
                
                if ( slow == fast ):
                    return True
                
                slow = slow.next
                fast = fast.next.next
                
        except:
            pass
        
        return False
        
def main():
    solution = Solution()
    
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = head
    
    
    print ( "True == " + str ( solution.hasCycle(head) ) ) 

if __name__ == "__main__":
    main()
        