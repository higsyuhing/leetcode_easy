class Solution {
public:
    bool isSubsequence(string s, string t) {
        // FSM... same as a simple parser.. 
        if(s.size() == 0) return true; 
        if(t.size() == 0) return false; 
        
        int i, j; 
        i = 0; j = 0; 
        char target = s[j]; 
        while(1){
            if(j == s.size()) return true; 
            if(i == t.size()) return false; 
            
            if(t[i] == target){
                j++; 
                target = s[j]; 
            }
            i++; 
        }
    }
};
