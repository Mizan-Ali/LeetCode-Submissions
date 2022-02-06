class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        uniq = nums[0]
        uniqCount = 1
        for i in range(1, n):
            if nums[i] == uniq:
                if uniqCount < 2:
                    uniqCount += 1
                elif uniqCount >= 2:
                    nums[i] = '_'
            else:
                uniq = nums[i]
                uniqCount = 1
        i = 0 
        j = 1
        while j < n:
            if nums[i] != '_':
                i += 1
                j += 1
            else:
                while j < n and nums[j] == '_':
                    j += 1
                if j < n:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        k = 0
        while k < n and nums[k] != '_':
            k += 1
        return k