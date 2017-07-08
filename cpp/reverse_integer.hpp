//
//  reverse_integer.h
//  LeetCode
//
//  Created by CLAYTON WONG on 7/5/17.
//  Copyright © 2017 Wong. All rights reserved.
//

#ifndef reverse_integer_h
#define reverse_integer_h


#endif /* reverse_integer_h */

/*
 
 7. Reverse Integer
 
 https://leetcode.com/problems/reverse-integer/#/description
 
 Reverse digits of an integer.
 
 Example1: x = 123, return 321
 Example2: x = -123, return -321
 
 */


#include <stdio.h>
#include <cmath>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        
        long result = 0;
        
        bool isNeg = false;
        if (x<0) {
            isNeg = true;
        }
        
        x = abs(x);
        while ( x > 0){
            result *= 10;
            result += x % 10;
            x/=10;
        }
        
        // overflow
        if ( result > pow(2,31)-1 ){
            return 0;
        }
        
        
        return isNeg ? -1 * (int)result : (int)result;
    }
};
