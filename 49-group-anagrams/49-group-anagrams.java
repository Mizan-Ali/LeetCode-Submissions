class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> hmap = new HashMap<>();
        
        for(int i=0; i<strs.length; i++) {
            char[] chararr = strs[i].toCharArray();
            Arrays.sort(chararr);
            String key = String.valueOf(chararr);
            if(!hmap.containsKey(key))
                hmap.put(key, new ArrayList<String>());
            hmap.get(key).add(strs[i]);
        }
        return new ArrayList<>(hmap.values());
    }
}