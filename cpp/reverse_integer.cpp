//
//  reverse_integer.cpp
//  LeetCode
//
//  Created by CLAYTON WONG on 7/5/17.
//  Copyright © 2017 Wong. All rights reserved.
//

#include <iostream>
#include "reverse_integer.hpp"

using namespace std;

int main(int argc, const char * argv[]) {
    
    
    Solution solution;
    
    cout << "123 == " << solution.reverse(123) << ": ";
    if (solution.reverse(123) != 321){
        cout << "Failed";
    } else {
        cout << "Passed";
    }
    cout << endl;
    
    cout << "-123: ";
    if (solution.reverse(-123) != -321){
        cout << "Failed";
    } else {
        cout << "Passed";
    }
    cout << endl;
    
    cout << "0: ";
    if ( solution.reverse(0) != 0 ){
        cout << "Failed";
    } else {
        cout << "Passed";
    }
    cout << endl;
    
    cout << "1: ";
    if ( solution.reverse(1) != 1 ){
        cout << "Failed";
    } else {
        cout << "Passed";
    }
    cout << endl;
    
    return 0;
}
