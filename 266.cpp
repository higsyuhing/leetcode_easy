class Solution {
public:
    bool canPermutePalindrome(string s) {
        int histo[26]; 
        for(int i = 0; i < 26; i++) histo[i] = 0; 
        for(int i = 0; i < s.size(); i++){
            histo[((int)(s[i] - 'a'))]++; 
        }
        
        int oddnum = 0; 
        for(int i = 0; i < 26; i++){
            if(histo[i] % 2 == 1) oddnum++; 
        }
        
        return (oddnum <= 1); 
    }
};
