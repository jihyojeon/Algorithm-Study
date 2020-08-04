class Solution:
    def brute_force_threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        candidate = sorted([nums[i], nums[j], nums[k]])
                        if candidate not in answers:
                            answers.append(candidate)
        return answers

    def left_threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                left = 0 - (nums[i] + nums[j])
                if left in nums[j + 1:]:
                    candidate = sorted([nums[i], nums[j], left])
                    if candidate not in answers:
                        answers.append(candidate)
        return answers

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     answers = []
    #     nums.sort()
    #     for i in range(len(nums) - 1):
    #         if i >= 1 and nums[i] == nums[i - 1]:
    #             continue
    #         left = i + 1
    #         right = len(nums) - 1
    #         while True:
    #             if left == right:
    #                 break
    #             sum = nums[i] + nums[left] + nums[right]
    #             if sum < 0:
    #                 left += 1
    #             elif sum > 0:
    #                 right -= 1
    #             else:
    #                 answers.append([nums[i], nums[left], nums[right]])
    #                 break
    #
    #     return answers