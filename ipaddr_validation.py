"""

468. Validate IP Address


Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.


"""

import re

IPV4 = "IPv4"
IPV6 = "IPv6"
INVALID = "Neither"

regex4 = re.compile("^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$")

regex6 = re.compile ( \
      "^([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)\:" \
    + "([0-9a-fA-F]+)$" )

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        #
        # validate input
        #
        if IP is None:
            return INVALID
        
        #
        # IPv4
        #
        if self.isValidIPV4Address(IP):
            return IPV4
        
        #
        # IPv6
        #
        elif self.isValidIPV6Address(IP):
            return IPV6
        
        #
        # Neither IPv4 nor IPv6
        #
        else:
            return INVALID 
        
    
    def isValidIPV4Address(self, IP):
        """
        :type IP: str
        :rtpye: bool
        """
        
        #
        # use regex to check for 4 "chunks" of IPv4 values
        #
        res = regex4.match(IP)
        
        if res is None:
            return False
        
        #
        # ensure each IPv4 value is valid
        #
        for grp in res.groups():
            if not self.isValidIPV4Value(grp):
                return False
             
        #
        # if all previous checks pass, then it is valid
        #
        return True
    
    
    def isValidIPV4Value(self, val):
        """
        :type val: int
        :rtype bool
        """
        
        #
        # ensure val is an integer between 0-255 inclusive
        #
        if int(val) < 0 or int(val) > 255:
            return False
        
        #
        # if val is 0, then ensure that it is only one 0
        #
        if int(val) == 0 and len(val) > 1:
            return False
        
        #
        # is val is not 0, then ensure that it does NOT start with 0
        #
        if int(val) != 0 and val[0] == '0':
            return False
        
        return True
    
    
    def isValidIPV6Address(self, IP):
        """
        :type IP: str
        :rtype: bool
        """
        
        #
        # use regex to check for 8 "chunks" of IPv6 values
        #
        res = regex6.match(IP)
        
        if res is None:
            return False
        
        #
        # ensure each IPv6 value is valid
        #
        for grp in res.groups():
            if not self.isValidIPV6Value(grp):
                return False
            
        #
        # if all previous checks pass, then it is valid
        #
        return True
    
    
    def isValidIPV6Value(self, val):
        """
        :type val: int
        :rtype bool
        """
        
        #
        # there should be at most 4 digits
        #
        if len(val) > 4:
            return False
        
        #
        # if all previous checks pass, then it is valid
        #
        return True
    
    
def main():
     
    
    
    solution = Solution()
    
    print ("IPv4 == " + str ( solution.validIPAddress("172.0.254.1") ))
    
    print ("Neither == " + str ( solution.validIPAddress("172.00.254.1") ))
    
    print ("Neither == " + str ( solution.validIPAddress("172.000.254.1") ))
    
    print ("Neither == " + str ( solution.validIPAddress("172.000.254.01") ))
    
    print ("Neither == " + str ( solution.validIPAddress("") ))
    
    print ("Neither == " + str ( solution.validIPAddress(None) ))

    print ("Neither == " + str ( solution.validIPAddress("....") ))


    print ("IPv6 == " + str ( solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")))
    
    print ("Neither == " + str ( solution.validIPAddress("2001: db8:85a3:0:0:8A2E:0370:7334")))
    
    print ("Neither == " + str ( solution.validIPAddress("2001:00:85a3:0:0:8A2E:0370:7334")))
    
    print ("Neither == " + str ( solution.validIPAddress("2001:000:85a3:0:0:8A2E:0370:7334")))
    
    print ("IPv6 == " + str ( solution.validIPAddress("2001:0000:85a3:0:0:8A2E:0370:7334")))
    
    print ("Neither == " + str ( solution.validIPAddress(":::::::")))
    
    print ("IPv6 == " + str ( solution.validIPAddress("0:0:0:0:0:0:0:0")))
    
    
    print ("Neither == " + str ( solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:")))

if __name__ == '__main__':
    main()





