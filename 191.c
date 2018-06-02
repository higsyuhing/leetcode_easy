int hammingWeight(uint32_t n) {
    int i; 
    int res = 0; 
    for(i = 0; i < 32; i++ ){
        res += (n & 0x1); 
        n = n >> 1;
    }
    return res; 
}
