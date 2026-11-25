class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        running_product = 1
        for i in range(1,len(nums)):
            num = nums[i-1] * running_product
            res[i] = num
            running_product = num
        running_product = 1
        for i in range(len(nums)-2, -1, -1):
            num = nums[i+1] * running_product
            res[i] *= num
            running_product=num
        return res