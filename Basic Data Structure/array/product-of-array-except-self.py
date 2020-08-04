class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(0,len(nums)-1):
            left.append(nums[i]*left[i])
        answer = []
        print(left)
        p = 1
        for i in range(len(nums)-1,-1,-1):
            left[i] = left[i] * p
            p = p * nums[i]

        return left