class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // this is a simple priority queue in c++
        
        priority_queue<int> pri_queue; 
        for(int i = 0; i < stones.size(); i++)
            pri_queue.push(stones[i]); 
        
        while(pri_queue.size() >= 2){
            int large = pri_queue.top(); 
            pri_queue.pop(); 
            int small = pri_queue.top(); 
            pri_queue.pop(); 
            
            if(large > small)
                pri_queue.push(large - small); 
        }
        
        if(pri_queue.empty()) return 0; 
        else return pri_queue.top(); 
    }
};
