"""

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = None
        
        if ( l1 is None or l2 is None ):
            return None
        
        curr_carry_over = 0
        prev_carry_over = 0
        itr1 = l1
        itr2 = l2
        
        itr_answer = None
        
        try:
            
            while ( True):
                

                l1_val = 0
                l2_val = 0
                
                #
                # exit when we have exhausted both lists
                #
                if ( l1 is None and l2 is None ):
                    break;
                
                #
                # add l1 and l2 values together
                #
                if ( l1 ):
                    l1_val = l1.val
                    
                if ( l2 ):
                    l2_val = l2.val
                    
                sum = l1_val + l2_val
                
                #
                # make sum the single digit value, and keep track of carry over
                #
                prev_carry_over = curr_carry_over
                
                if ( sum >= 10 ):
                    curr_carry_over = 1
                    sum %= 10
                else:
                    curr_carry_over = 0
                
                #
                # first iteration, create a new linked list
                #
                if ( itr_answer is None ):
                    itr_answer = ListNode( sum )
                    answer = itr_answer
                
                #
                # append onto existing linked list by
                # adding each list and keeping track of carry overs
                #
                else:
                    #
                    # check if adding the previous carry over causes current carry over
                    #
                    if ( sum + prev_carry_over == 10 ):
                        curr_carry_over = 1
                        sum = 0
                    else:
                        sum += prev_carry_over
                       
                    itr_answer.next = ListNode ( sum )
                    itr_answer = itr_answer.next
                    
                if ( l1 ):
                    l1 = l1.next
                    
                if ( l2 ):
                    l2 = l2.next
            
        except: 
            pass
        
        if ( curr_carry_over ):
            itr_answer.next = ListNode ( 1 )
        
        return answer
    
def main():
    solution = Solution()
    
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    print ( "2->4->3 + 5->6->4 = 342 + 465 = 807 == 7->0->8: " )
    
    import pdb
    pdb.set_trace()
    
    answer = solution.addTwoNumbers(l1, l2)
    
    itr = answer
    
    while ( itr ):
        print ( itr.val )
        itr = itr.next
        
    
if __name__ == "__main__":
    main()