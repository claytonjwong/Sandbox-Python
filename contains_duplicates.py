"""

217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.



"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len ( nums )
        hash = {}
        
        #
        # go through each number and see if it exists in the hash table
        #
        # if the lookup fails, KeyError exception is thrown,
        # so add the num to hash
        #
        for num in nums:
            try:
                #
                # see if duplicate already exists
                #
                if ( hash[num] ):
                    return True
                
            except KeyError:
                #
                # add first time entry
                #
                hash[num] = True
    
        return False
    
def main():
    
    solution = Solution()
    print("True == " + str ( solution.containsDuplicate([0,1,2,3,4,4,5]) ) )
    

if __name__ == "__main__":
    main()







