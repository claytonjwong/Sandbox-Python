"""

203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        curr = head
        prev = None
        
        while ( curr ):
            
            #
            # remove elements of the linked list, by setting prev.next to curr.next
            #
            if ( curr.val == val ):
                
                #
                # an AttributeError exception will be throw when prev is None,
                # this occurs for the first element of the linked list
                #
                try:
                    #
                    # remove the current element
                    #
                    prev.next = curr.next
                    
                    #
                    # set curr to the next element
                    #
                    curr = curr.next
                    
                except AttributeError:
                    
                    #
                    # remove the head by setting curr to the next element,
                    # then set head to curr
                    #
                    curr = curr.next
                    head = curr
            
            #
            # the value does NOT match, keep the element, and iterate forward
            #
            else:
                prev = curr
                curr = curr.next

        return head

def main():
    
    solution = Solution()
    
    ll = ListNode(0)
    ll.next = ListNode(1)
    ll.next.next = ListNode(2)
    

    new_ll = solution.removeElements(ll, 2)


if __name__ == "__main__":
    main()


