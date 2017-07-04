"""

278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(version):
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.firstBadVersionHelper(1, n)

    
    def firstBadVersionHelper(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        
        #
        # end recursion whe start is equal to the end
        # this is the first instance of a bad version
        #
        if start == end:
            return end

        #
        # see if the middle of the current values is a bad version,
        # then recursively check the half which contains a bad version
        # in order to find the first instance
        #
        mid = ( start + end ) // 2
        
        if isBadVersion(mid):
            return self.firstBadVersionHelper(start, mid)
        else:
            return self.firstBadVersionHelper(mid+1, end)
        
    
    
def main():
    pass

if __name__ == "__main__":
    main()
    
    
    
    
    