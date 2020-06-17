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

/*
class Solution {
public:
    int getSum(int a, int b) {
        if(!a) return b;
        return getSum(( (a&b) & 0xffffffff )<<1,a^b);
    }
};
*/
