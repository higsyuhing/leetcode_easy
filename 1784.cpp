class Solution {
public:
    bool checkOnesSegment(string s) {
        // 2 cases: 11...11, 11..10..xx
        bool haszero = false; 
        for (char &c : s){
            if (c == '0'){
                if (haszero == false)
                    haszero = true; 
            }
            else{
                if (haszero == true) return false; 
            }
        }

        return true; 
    }
};
