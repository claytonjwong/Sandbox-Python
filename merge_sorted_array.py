"""

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2. The number of elements initialized in nums1 and nums2
are m and n respectively.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        #
        # use nums1_itr to iterate through nums1
        #
        nums1_index = 0

        #
        # iterate through nums2 and insert into nums1
        #
        for num in nums2:
            
            #
            # we have reached the end of nums1 sorted array
            # so the current position should be available
            #
            if ( nums1_index >= m  ):
                nums1.insert ( nums1_index, num )
                nums1_index += 1
            
            #
            # find the appropriate position within nums1 and insert there
            #
            else:

                while ( num > nums1 [ nums1_index ] and nums1_index < m ):
                    nums1_index += 1
            
                nums1.insert ( nums1_index, num )
                
                #
                # since we have inserted into the middle of num1 somewhere,
                # increment m to keep track of the current length
                # of non-dummy entries of num1, this is needed to know when
                # we have reached the new end of num1, since num1 is growing
                #
                m += 1
            
            #
            # remove dummy holder position from the end of num1 list
            # we do this regardless if the number was inserted
            # in the middle of num1 list or at the end of num1 list
            #
            nums1.pop ( len ( nums1 ) - 1 )
            
                

            

    
    
def main():
    



    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print ( "[1] == " + str ( nums1 ) )



    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print ( "[1, 2, 2, 3, 5, 6] == " + str ( nums1 ) )
    
    

    
    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print ( "[1, 2] == " + str ( nums1 ) ) 
    
    
if __name__ == "__main__":
    main()
    
    