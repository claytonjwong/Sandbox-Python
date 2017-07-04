"""

Reverse a linked list

Input: 1->2->3
Output: 3->2->1


"""




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def rev(self, head):
        """
        :type head: ListNode
        :rtype: None
        """
        
        curr, prev = head, None
        
        while curr and curr.next:
            
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            
        curr.next = prev
            
        return curr

    
    def pprint(self, head):
        """
        :type head: ListNode
        :rtype: None
        """
        
        itr = head
        str_ll = "["
        while itr:
            str_ll += str(itr.val) + ","
            itr=itr.next
            
        return str_ll[:len(str_ll)-1] + "]"
    
def main():
    
    solution = Solution()
    
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    

    print ( "before: " + solution.pprint(l1) )
    l1 = solution.rev(l1)
    print ( "after: " + solution.pprint(l1) )



if __name__ == '__main__':
    main()
    
    
    
    
    
    