class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # we can apply bfs
        queue = [(0, 0)] # (node, level)
        visited = [False for _ in range(len(nums))]
        while queue:
            curr, level = queue.pop(0)
            for i in range(curr+1, curr+nums[curr]+1):
                if i == len(nums)-1:
                    return level+1
                if visited[i] == False:
                    visited[i] = True
                    queue.append((i, level+1))
