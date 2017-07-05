"""

Given a sorted linked list, delete all duplicates such that each element appear only once. 

For example,
 Given 1->1->2, return 1->2.
 Given 1->1->2->3->3, return 1->2->3. 


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        
        linked_list_str = str ( self.val )
        
        itr = self.next
        while ( itr ):
            
            linked_list_str = linked_list_str + "->" + str ( itr.val )           
            itr = itr.next
        
        return linked_list_str

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #
        # linked list length is 0
        #
        if ( not head ):
            return None
        
        #
        # linked list length is 1
        #
        elif ( head and not head.next ):
            return head
        
        #
        # curr and curr.next exist, iterate
        # through the linked list
        #
        prev = head
        curr = head.next
        
        while ( curr ):
            
            #
            # remove the duplicate node by bypassing it
            # such that the previous next is no longer current
            # but current.next instead
            #
            if ( prev.val == curr.val ):
                prev.next = curr.next
            #
            # not a duplicate, move prev to curr in preparation
            # for comparing the next nodes for dups
            #
            else:
                prev = curr
            
            #
            # iterate to the next node in the linked list
            #
            curr = curr.next
    
        #
        # return the new linked list with duplicates removed
        #
        return head
    
    
def main():
    
    solution = Solution()
    
    linked_list = ListNode(1)
    linked_list.next = ListNode(1)
    linked_list.next.next = ListNode(1)
    
    print ( "1 == " + str ( solution.deleteDuplicates(linked_list) ) )
    
    
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    
    print ( "1->2->3 == " + str ( solution.deleteDuplicates(linked_list) ) )
    
    
if __name__ == "__main__":
    main()