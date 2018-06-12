class Solution {
public:
    int getSum(int a, int b) {
        int c = 0;
        while(b)
        {
            c = b;
            b = (a & b) << 1;
            a = a ^ c;
        }
        return a;
    }
};
