class Solution {
public:
    int removePalindromeSub(string s) {
        // based on hint 2.... so boring this question... 
        
        // check if we can do it in 1 remove
        int i, j, onemove; 
        i = 0; j = s.size()-1; onemove = 1; 
        while (i < j){
            if (s[i] != s[j]){
                onemove = 0; 
                break; 
            }
            i++; 
            j--; 
        }
        
        if (onemove) return 1; 
        else return 2; 
    }
};
