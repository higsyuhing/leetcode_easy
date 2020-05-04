

void reverseString(char* s, int sSize){
    char tempc; 
    int curr; 
    for(curr = 0; curr < (sSize/2); curr++){
        tempc = s[curr]; 
        s[curr] = s[sSize-1-curr]; 
        s[sSize-1-curr] = tempc;
    }
}
