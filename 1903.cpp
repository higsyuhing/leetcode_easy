class Solution {
public:
    string largestOddNumber(string num) {
        // 2 steps
        
        // find the odd number from right to left. 
        int len = num.size(); 
        int i; 
        for (i = 0; i < len; i++){
            char c = num[len - 1 - i]; 
            if ( ((unsigned)(c - '0')) % 2 == 1 ) break; 
        }
        
        return num.substr(0, len - i); 
    }
};
