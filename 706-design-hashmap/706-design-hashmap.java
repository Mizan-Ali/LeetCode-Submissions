class MyHashMap {
    int[] hmap;
    public MyHashMap() {
        hmap = new int[(int)Math.pow(10, 6)+1];
        Arrays.fill(hmap, -1);
    }
    
    public void put(int key, int value) {
        hmap[key] = value;
    }
    
    public int get(int key) {
        return hmap[key];
    }
    
    public void remove(int key) {
        hmap[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */