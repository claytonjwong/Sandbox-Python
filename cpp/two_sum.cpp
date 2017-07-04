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
                	result.push_back(j);
                	result.push_back(i);
                	break;
                }
            }
        }

        return result;
    }
};

int main() {

	Solution* solution = new Solution();

	vector<int> nums;
	nums.push_back(15);
	nums.push_back(11);
	nums.push_back(7);
	nums.push_back(2);

	for (int i=0; i<nums.size(); i++){
		cout << i << ": " << nums[i] << endl;
	}

	vector<int> retval = solution->twoSum(nums, 9);

	cout << "[0,1] == " << "[" << nums[0] << "," << nums[1] << "]" << endl;



	return 0;
}
