class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            second = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] == second:
                    return [i, j]
    