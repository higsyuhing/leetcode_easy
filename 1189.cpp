class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int histo[26]; 
        for(int i = 0; i < 26; i++) histo[i] = 0;
        for(int i = 0; i < text.size(); i++){
            histo[text[i] - 'a']++; 
        }
        
        int curr = histo[0]; // a
        curr = min(curr, histo[1]); // b
        curr = min(curr, histo[11]/2); // ll
        curr = min(curr, histo[14]/2); // oo
        curr = min(curr, histo[13]); // n
        return curr; 
    }
};
