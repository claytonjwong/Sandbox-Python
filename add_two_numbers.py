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

    def __str__(self):
        
        val = "["
        
        itr = self
        while ( itr ):
            val += str(itr.val) + ", "
            itr = itr.next
        
        #
        # do not include the last comma space
        #
        return val[0:len(val)-2] + "]"
    

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
        
        list1 = []
        list2 = []
        
        #
        # push values into list which is left-padded with 0s
        #
        len_l1 = 0
        while itr1 is not None:
            len_l1 += 1
            itr1 = itr1.next
            
        len_l2 = 0
        while itr2 is not None:
            len_l2 += 1
            itr2 = itr2.next
            
        if len_l1 > len_l2:
            
            i = len_l1 - len_l2
            
            while i > 0:
                new_node = ListNode(0)
                new_node.next = l2
                l2 = new_node
                i -= 1
                
        if len_l2 > len_l1:
            
            i = len_l2 - len_l1
            
            while i > 0:
                new_node = ListNode(0)
                new_node.next = l1
                l1 = new_node
                i -= 1
        
        #
        # linked list lengths are the same, now that they are 0 filled
        #
        i = 0
        itr1 = l1
        itr2 = l2
        while i < max ( len_l1, len_l2 ):
            
            list1.append(itr1.val)
            itr1 = itr1.next
            
            list2.append(itr2.val)
            itr2 = itr2.next
            
            i += 1
        

        itr_answer = None
        

        i = max ( len_l1, len_l2 ) - 1
        while ( i >= 0 ):
        
            l1_val = list1[i]
            l2_val = list2[i]
                
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
                   
                #
                # append value onto the front of the linked list
                #
                temp = ListNode ( sum )
                temp.next = answer
                answer = temp
            
            #
            # iterate through the lists from right to left
            #
            i -= 1
        
        #
        # check for one last carry over, and append onto the front
        #
        if ( curr_carry_over ):
            temp = ListNode(1)
            temp.next = answer
            answer = temp
        
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
     
 
     
    print ( solution.addTwoNumbers(l1, l2) )
     

    
    
    
    # [7,2,4,3]
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    
    # [5,6,4]
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    
    
    print (  solution.addTwoNumbers(l1, l2) )
    
    
    l1 = ListNode(9)
    l2 = ListNode(1)
    
    print (  "10 == " + str ( solution.addTwoNumbers(l1, l2)  ))
    
    
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l2 = ListNode(1)
    
    
    
    print (  "1000 == " + str ( solution.addTwoNumbers(l1, l2)  ))
    
            
if __name__ == "__main__":
    main()