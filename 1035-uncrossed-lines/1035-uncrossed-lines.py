class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # Longest common subsequence
        dp = {}
        def solve(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i, j) not in dp:
                if nums1[i] == nums2[j]:
                    dp[(i, j)] = 1 + solve(i+1, j+1)
                else:
                    dp[(i, j)] = max(solve(i+1, j+1), solve(i+1, j), solve(i, j+1))
            return dp[(i, j)]

        i, j = 0, 0
        return solve(i, j)