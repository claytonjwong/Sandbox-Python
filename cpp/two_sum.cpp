/*

1. Two Sum

https://leetcode.com/problems/two-sum/#/description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

 */

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

    	vector<int> result;

        for (int i=0; i < nums.size() - 1; i++) {
            for (int j=i+1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                	result.push_back(i);
                	result.push_back(j);
                	break;
                }
            }
        }

        return result;
    }
};

int main() {

	Solution solution;

	vector<int> nums;
	nums.push_back(2);
	nums.push_back(7);
	nums.push_back(11);
	nums.push_back(15);

	for (int i=0; i<nums.size(); i++){
		cout << i << ": " << nums[i] << endl;
	}

	vector<int> retval = solution.twoSum(nums, 9);

	cout << "[0,1] == " << "[" << retval[0] << "," << retval[1] << "]" << endl;



	return 0;
}
