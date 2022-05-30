class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if (arr.size() < 3)
        {
            return false; 
        }
        
        int state = 0; // 0: increase, 1: descrease
        int last = arr[0]; 
        for (int i = 1; i < arr.size(); i++)
        {
            int curr = arr[i]; 
            if (state == 0)
            {
                if (curr == last) return false; 
                if (curr < last)
                {
                    if (i == 1) return false; 
                    state = 1; 
                }
                last = curr; 
            }
            else
            {
                if (curr < last)
                {
                    last = curr; 
                }
                else return false; 
            }
        }
        
        if (state == 0) return false; 
        else return true; 
    }
};
