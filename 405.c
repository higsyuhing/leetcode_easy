char* toHex(int num) {
    char *res; 
    if(num == 0){
        res = malloc(2); 
        res[0] = '0';
        res[1] = '\0'; 
        return res; 
    }
    uint32_t temp = num; 
    uint32_t curr = 0; 
    int index;
    int flag = -1; 
    for(index = 8; index > 0; index--){
        curr = (temp & (0xf0000000)) >> 28; 
        temp = temp << 4; 
        if(curr == 0 && flag == -1){
            continue; 
        }
        else{
            if(flag == -1){
                res = (char *)malloc(index+1);
                flag = index; 
                if(curr < 10){
                    res[flag-index] = 48 + curr; 
                }
                else{
                    res[flag-index] = 87 + curr; 
                }
            }
            else{
                if(curr < 10){
                    res[flag-index] = 48 + curr; 
                }
                else{
                    res[flag-index] = 87 + curr; 
                }
            }
        }
    }
    res[flag] = '\0'; 
    return res; 
}
