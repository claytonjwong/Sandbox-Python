"""

234. Palindrome Linked List


https://leetcode.com/problems/palindrome-linked-list/tabs/description


Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        string_so_far = []
        while(head):
            string_so_far += head.val,
            head=head.next
        return string_so_far==string_so_far[::-1]
        
        
        
        
        
if __name__ == '__main__':
    
    solution = Solution()
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    
    print(str("isPalindrome == " + solution.isPalindrome(head)))
    
    
    
    
    