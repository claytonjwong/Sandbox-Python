"""

24. Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/#/description

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.


"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #
        # sanity checks
        #
        if head is None:
            return None

        
        if head.next is None:
            return head
    
        #
        # swap prev.next and curr.next
        # using staggered curr/prev in sliding window as follow
        #
        # None  head  head.next
        # p1    c1
        #       p2    c2
        #
        p1, c1 = None, head
        p2, c2 = head, head.next
               
        while True:
            #
            # make p1 point to c2
            #
            # and
            #
            # make p2 point to c1
            #
            if p1 is None: # special case for first iteration
                head = c2
            else:
                p1.next = c2
    
            p2.next = c1
            
            #
            # swap c1 next and c2 next 
            #
            temp = c1.next
            c1.next = c2.next
            c2.next = temp
                       
            #
            # iterate to next pair
            #
            if c1.next and c1.next.next:
                p1, c1 = c1, c1.next
                p2, c2 = c1, c1.next
            else:
                break
            
        
        return head
        
        
    
    def print_list(self, head):
        """
        :type head: ListNode
        :rtype: None
        """
        
        result = "["
        
        itr=head
        while itr:
            
            result += str(itr.val) + ","
            
            itr = itr.next
        
        print ( result[:-1] + "]" )
            
    
def main():
    solution = Solution()
    
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)
    
    
    print ( "Before: " )
    solution.print_list(l1)
    


    l1 = solution.swapPairs(l1)
    
    print ( "\n\n\nAfter: " )
    solution.print_list(l1)
    
    
    l2 = None
    l2 = solution.swapPairs(l2)
    
    print ("None == " + str ( l2 ) )
    
    l2 = ListNode(1)
    l2 = solution.swapPairs(l2)
    
    print ("[1] == ")
    solution.print_list(l2)
    
    
    
if __name__ == '__main__':
    main()
    
    
    



