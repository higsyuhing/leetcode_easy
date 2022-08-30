class Foo {
private: 
    atomic<int> order; 
    
    // using CV and semaphore are both good. I prefer CV.. 
    
public:
    Foo() {
        order = 0; 
    }

    void first(function<void()> printFirst) {
        // while(1){
        //     bool ret = order.compare_exchange_strong(0, 1, std::memory_order_seq_cst); 
        //     if (ret) break; 
        // }
        // while (order != 0); 
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        
        // order.fetch_add(1); 
    }

    void second(function<void()> printSecond) {
        // while(!order.compare_exchange_strong(1, 2, std::memory_order_seq_cst)); 
        // while(1){
        //     bool ret = order.compare_exchange_strong(1, 2, std::memory_order_seq_cst); 
        //     if (ret) break; 
        // }
        // while (order != 1); 
        
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        
        // order.fetch_add(1); 
    }

    void third(function<void()> printThird) {
        // while(!order.compare_exchange_strong(2, 0, std::memory_order_seq_cst)); 
        // while(1){
        //     bool ret = order.compare_exchange_strong(2, 0, std::memory_order_seq_cst); 
        //     if (ret) break; 
        // }
        // while (order != 2); 
        
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        
        // order.exchange(0); 
    }
};
