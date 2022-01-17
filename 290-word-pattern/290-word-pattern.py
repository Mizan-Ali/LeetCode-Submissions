class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(set(s)) != len(set(pattern)):
            return False
        if len(s) != len(pattern):
            return False
        
        test_map = {}
        test_map1 = {}
        for key, val in zip(pattern, s):
            if key not in test_map:
                test_map[key] = val
            else:
                if test_map[key] != val:
                    return False
            if val not in test_map1:
                test_map1[val] = key
            else:
                if test_map1[val] != key:
                    return False
        return True