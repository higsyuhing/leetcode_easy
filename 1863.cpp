class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        // nums.length < 13, then we can use a unsigned integer for the select mask
        
        int res = 0;
        for (auto i = 1; i < (1 << nums.size()); ++i) {
            int total = 0;
            for (auto j = 0; j < nums.size(); ++j)
                if (i & (1 << j))
                    total ^= nums[j];
            res += total;
        }
        return res;
        
        
        
    }
};

/*

int subsetXORSum(vector<int>& nums,int sum=0) {
    for(int n:nums)
        sum|=n;
    return sum*pow(2,nums.size()-1);
}

    int subsetXORSum(vector<int>& nums) {
        return allSubs(0, nums, 0);
    }
    
    int allSubs(int cur, vector<int>& nums, int xoR) {
        if (cur == nums.size()) {
            return xoR;
        }
        // Include
        int include = allSubs(cur + 1, nums, nums[cur] ^ xoR);
        // Exclude
        int exclude = allSubs(cur + 1, nums, xoR);
        return include + exclude;
    }



*/
