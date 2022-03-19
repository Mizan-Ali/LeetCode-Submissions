class FreqStack {
        Map<Integer, Integer> freqMap;
        Map<Integer, Stack<Integer>> stackMap;
        Integer maxFreq;
    
    public FreqStack() {
        freqMap = new HashMap();
        stackMap = new HashMap();
        maxFreq = -1;
    }
    
    public void push(int val) {
        int f = freqMap.getOrDefault(val, 0) + 1;
        freqMap.put(val, f);
        maxFreq = Math.max(maxFreq, f);
        
        if(!stackMap.containsKey(f)) {
            stackMap.put(f, new Stack());
        }
        stackMap.get(f).push(val);
    }
    
    public int pop() {
        int ans = stackMap.get(maxFreq).pop();
        freqMap.put(ans, freqMap.get(ans)-1);
        
        if(stackMap.get(maxFreq).isEmpty()) {
            maxFreq--;
        }
        return ans;
    
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */