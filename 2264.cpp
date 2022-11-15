class Solution {
public:
    string largestGoodInteger(string num) {
        int target = -1; 
        int count = 0; 
        int val = -1; 
        for (char &c : num){
            int curr = (int)(c - '0'); 
            if (curr != val){
                val = curr; 
                count = 1; 
            }
            else{
                count++; 
                if ((count > 2) && (val > target))
                    target = val; 
            }
        }

        if (target == -1) return ""; 
        else return string(3, '0'+target); 
    }
};
