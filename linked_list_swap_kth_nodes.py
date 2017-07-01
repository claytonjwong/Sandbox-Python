"""

linked list swap Kth node from the left with the Kth node from the right

examples:

input: [1,2,3,4,5] k=2
output: [1,4,3,2,5]

input: [1,2,3,4,5,6] k=4
output: [1,2,4,3,5,6]

"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        #
        # sanity checks
        #
        if head is None or k==0:
            return head
        
        #
        # first find the curr and prev of the nodes
        # to be swapped based on the linked list length
        #
        k_from_left_curr, k_from_left_prev = None, None
        k_from_right_curr, k_from_right_prev = None, None
        
        #
        # k-nodes from left node inclusive
        #
        i=1
        curr, prev = head, None
        while curr is not None:

            if i == k:
                k_from_left_curr = curr
                k_from_left_prev = prev
                #
                # do NOT break here, we need to iterate
                # through the entire linked list
                # to find the length of the linked list
                # this will be used to find the k-nodes from the right
                #
            if curr.next is not None:
                i+=1

            prev = curr
            curr=curr.next
        #
        # use i for the length of the linked list,
        # this is needed in order to find the Kth node
        # from the right
        #
        list_len = i
        
        #
        # if k > the length of the list, then there are no nodes to swap,
        # since traversing the linked list from left-to-right or from right-to-left
        # will go past the end of the linked list, so just return the unmodified linked list
        #
        if k > list_len:
            return head
        #
        # k-nodes from right node inclusive
        #
        i=1
        curr, prev = head, None
        while curr is not None:
            
            if i == list_len - k + 1:
                k_from_right_curr = curr
                k_from_right_prev = prev
                break
                
            prev = curr
            curr = curr.next
            i += 1
        
        head = self.swapNodesHelper( \
            head, \
            k_from_left_curr, k_from_left_prev, \
            k_from_right_curr, k_from_right_prev )
    
        return head


    def swapNodesHelper(self, head, c1, p1, c2, p2):
        """
        :type head: ListNode
        :type c1: ListNode
        :type p1: ListNode
        :type c2: ListNode
        :type p2: ListNode
        :rtype: ListNode
        """
        
        #
        # swap previous.next to point towards new current nodes
        #
        # current 1's previous node now points to current 2
        # current 2's previous node now points to current 1
        #
        if p1 is not None and p2 is not None: # neither c1 nor c2 are the head
            p1.next = c2
            p2.next = c1
            
        elif p1 is None: # c1 is the head, since p1 is None, make c2 the new head
            head = c2
            p2.next = c1
            
        elif p2 is None: # c2 is the head, since p2 is None, make c1 the new head
            head = c1
            p1.next = c2
        #
        # swap current.next
        #
        temp = c1.next
        c1.next = c2.next
        c2.next = temp
        
        return head
        

    def print_list(self, msg, ll):
        
        #
        # construct pretty string
        #
        ps = msg + ": "
        itr=ll
        i=1
        ps += "["
        while itr:
            ps += str(itr.val) + ","
            itr=itr.next
            i += 1
        ps = ps[:len(ps)-1] + "]" # remove the last comma and add "]" instead
        
        print(ps)
    
        
def main():
    
    solution = Solution()
    
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    
    #
    # swap
    #
    solution.print_list("before", l1)
    result = solution.swapNodes( l1, 2 )
    solution.print_list("after ", result)

    #
    # same swap again, this should be the original linked list order
    #
    solution.print_list("before", result)
    result = solution.swapNodes( result, 2 )
    solution.print_list("after ", result)


    print("\n\n\n\n")


    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)
    l2.next.next.next = ListNode(4)
    l2.next.next.next.next = ListNode(5)
    l2.next.next.next.next.next = ListNode(6)    
    
    solution.print_list("before", l2)
    result = solution.swapNodes( l2, 4 )
    solution.print_list("after ", result)
    
    solution.print_list("before", result)
    result = solution.swapNodes( result, 4 )
    solution.print_list("after ", result)
     

    print("\n\n\n")
    

    solution.print_list("before", result)
    result = solution.swapNodes( result, 6 )
    solution.print_list("after ", result)
    
    solution.print_list("before", result)
    result = solution.swapNodes( result, 6 )
    solution.print_list("after ", result)


    print("\n\n\n")
    

    solution.print_list("before", result)
    result = solution.swapNodes( result, 7 )
    solution.print_list("after ", result)
    
    solution.print_list("before", result)
    result = solution.swapNodes( result, 7 )
    solution.print_list("after ", result)
    
    
    print("\n\n\n")
    

    solution.print_list("before", result)
    result = solution.swapNodes( result, 0 )
    solution.print_list("after ", result)
    
    solution.print_list("before", result)
    result = solution.swapNodes( result, 0 )
    solution.print_list("after ", result)
    
if __name__ == '__main__':
    main()
    
    
    
    