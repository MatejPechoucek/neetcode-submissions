class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []

        rp = 1

        for n in nums:
            r.append(rp)
            rp *= n
        
        rp = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] *= rp
            rp *= nums[i]
        return r