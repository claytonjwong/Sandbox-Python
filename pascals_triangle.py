"""

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
 Return 
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""


class Solution(object):
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        pt = []
        
        if ( numRows <= 0 ):
            return []
        
        if ( numRows == 1 ):
            return [[1]]
        
        
        #
        # more than 1 row, start with 1
        #
        pt.append([1])

        n = 1 # row
        k = 1 # column
        
        #
        # calculate the rest of the rows
        #
        while ( n < numRows ):
            
            #
            # create a new list for this row
            #
            pt.append([1])
            
            #
            # each row contains n - 1 columns
            # so iterate through the columns 1 to n - 1
            #
            while ( k < n ):
                
                #
                # add the previous row values (k-1, n-1) and (k, n-1)
                # in order to calculate the current value
                #
                prev1 = pt[n-1][k-1]
                prev2 = pt[n-1][k]

                pt[n].append(prev1 + prev2)
                
                #
                # next column
                #
                k += 1
                    
            #
            # append 1 at the end of this row
            #
            pt[n].append(1)
            
            #
            # next row
            #
            # set k = 1 because PT(n,k) = PT(n-1,k-1) and PT(n-1,k)
            # from the previous row in order to calculate the current row
            # so the first iteration will be previous row ( n-1 ),
            # first column 0 = k - 1 + second column 1 = k
            #
            n += 1
            k = 1 
            
        return pt
    
    
def main():
    
    solution = Solution()
    
    pt1 = solution.generate(1)
    pt2 = solution.generate(2)
    pt3 = solution.generate(3)
    
    import pdb
    pdb.set_trace()
    
if __name__ == "__main__":
    main()