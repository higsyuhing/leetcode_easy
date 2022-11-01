class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unsigned char allow[26]; 
        for (int i = 0; i < 26; i++) allow[i] = 0; 
        for (char c : allowed){
            allow[(int)(c - 'a')] = 1; 
        }
        
        unsigned char map[26];
        int res = 0; 
        for (auto &word : words){
            for (int i = 0; i < 26; i++) map[i] = 0; 
            for (char c : word){
                map[(int)(c - 'a')] = 1; 
            }
            int failflag = 0; 
            for (int i = 0; i < 26; i++){
                if (allow[i] < map[i]){
                    failflag = 1; 
                    break; 
                }
            }
            if (failflag == 0)
                res++; 
        }
        
        return res; 
    }
};
