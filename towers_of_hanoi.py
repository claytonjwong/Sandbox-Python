"""

Towers of Hanoi



Sample input/output:

Before:

A: [1, 2, 3]
B: []
C: []




After:

A: []
B: [1, 2, 3]
C: []


"""


class Solution(object):
    
    def move(self, m, src, dst, aux):
        
        # base case, no disks to move
        if m == 0:
            return
        
        # Step A) move m-1 disks from src to aux
        self.move(m-1, src, aux, dst) 
    
        
        # Step B) move Mth disk from src to dst
        if len(src) > 0:
            dst.insert(0, src.pop(0))

        # move m-1 disks from aux to dst
        self.move(m-1, aux, dst, src)


    def pretty_print(self, a,b,c):
        
        print ("A: " + str(A))
        print ("B: " + str(B))
        print ("C: " + str(C))
        print ("\n\n\n");
        
        
        
if __name__ == '__main__':
    
    solution = Solution()
    
    m = 3
    A = list(range(1,m+1))
    B = list()
    C = list()
    
    print("Before:\n")
    solution.pretty_print(A, B, C)

    solution.move(m, A, B, C)
    
    print("After:\n")
    solution.pretty_print(A, B, C)
    
    
    