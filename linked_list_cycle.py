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
        
        #
        # either fast will catch with slow
        # if there is a loop in the linked list
        #
        # or an exception will be throw after next is None
        #
        try:

            #
            # slow will move one link at a time
            #
            # fast will move two links at a time
            #
            slow = head
            fast = head.next
        
            while ( True ):
        
                if ( slow == fast ):
                    return True
                
                slow = slow.next
                fast = fast.next.next
        
        except:
            return False
            
    
def main():
    solution = Solution()
    
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    linked_list.next.next.next = linked_list

    
    print ( "True == " + str ( solution.hasCycle(linked_list) ) )
    
    
if __name__ == "__main__":
    main()