class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        leftSum = 0
        rightSum = sum(nums)
        ans = [0]*len(nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            ans[i] = abs(leftSum-rightSum)
            leftSum += nums[i]
        
        return ans