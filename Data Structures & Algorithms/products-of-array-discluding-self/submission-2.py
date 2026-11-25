class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        running_product = 1

        for num in nums:
            res.append(running_product)
            running_product *= num
        
        running_product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= running_product
            running_product *= nums[i]
        return res