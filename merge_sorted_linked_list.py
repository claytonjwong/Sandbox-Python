"""

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        
        pretty_str = ""
        
        curr = self
        
        while ( curr ):
            pretty_str = pretty_str + str ( curr.val ) + ", "
            curr = curr.next
        
        return pretty_str
        

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        
        c1 = l1
        c2 = l2
        c3 = dummy

        #
        # got through each list, and point "next" of the list we are returning
        # towards the list which contains the smaller value, we assume each list
        # is incremetally ordered
        #
        while ( c1 and c2 ):
            if ( c1.val < c2.val ):
                c3.next = c1
                c1 = c1.next
            else:
                c3.next = c2
                c2 = c2.next
            
            c3 = c3.next
        #
        # see if there is anything left of either list,
        # and add it onto the end
        # of the sorted list
        #
        if ( c1 ):
            c3.next = c1
        elif ( c2 ):
            c3.next = c2
        
    
        return dummy.next
    
        
def make_linked_list(array_list):
    
    linked_list = None
    curr = None
    
    #
    # reverse the ordered array_list, since we will be adding them
    # in reverse order onto this linked array_list
    #
    array_list.reverse()
    
    #
    # add each integer onto the linked array_list
    #
    for i in array_list:
        if linked_list == None:
            linked_list = ListNode(i)
            linked_list.next = None
        else:
            new_node = ListNode(i)
            new_node.next = linked_list
            linked_list = new_node
    
    return linked_list
        

def main():
    solution = Solution()
    
    listA = make_linked_list([1,2,3,4])
    listB = make_linked_list([1,2,3,4])
    listC = solution.mergeTwoLists(listA, listB)

    print ( "listC: 1,1,2,2,3,3,4,4 == " + str ( listC ))

if __name__ == "__main__":
    main()
        