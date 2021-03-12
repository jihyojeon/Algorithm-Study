class Solution:
    def brute_force_twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def using_in_twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            left = target - nums[i]
            last = nums[i + 1:]
            if left in last:
                return [i, last.index(left) + (i + 1)]

    def read_twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            nums_dict[num] = idx
        for idx, num in enumerate(nums):
            if target-num in nums_dict and nums_dict[target-num] != idx:
                return[idx, nums_dict[target-num]]