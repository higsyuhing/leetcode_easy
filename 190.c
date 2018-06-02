uint32_t reverseBits(uint32_t n) {
    int i;
    uint32_t res = 0; 
    for(i = 0; i < 32; i++){
        res = (res << 1) | (n & 0x1); 
        n = n >> 1; 
    }
    return res;
}
