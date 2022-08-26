class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        
        // use hash map to record the occurrence of each element
        // put the remaining in a vector
        // at the end construct the new vector with hashmap and remaining-vector
        
        map<int, int> hashmap; 
        for (int val : arr2){
            hashmap[val] = 0; 
        }
        
        vector<int> ret; // remaining vector, reuse
        for (int val : arr1){
            if (hashmap.count(val) == 0){
                // not our target, put into the ret. 
                ret.push_back(val); 
            }
            else{
                hashmap[val]++; 
            }
        }
        
        // sort
        sort(ret.begin(), ret.end()); 
        
        // construct the result array, reverse order of arr2
        for (auto it = arr2.rbegin(); it != arr2.rend(); it++){
            int val = *it; 
            ret.insert(ret.begin(), hashmap[val], val); 
        }
        
        return ret; 
        
    }
};
