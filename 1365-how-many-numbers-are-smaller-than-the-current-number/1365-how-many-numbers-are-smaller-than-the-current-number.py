class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            count = 0
            for num in nums:
                if nums[i] > num:
                    count += 1
            res.append(count)
        return res