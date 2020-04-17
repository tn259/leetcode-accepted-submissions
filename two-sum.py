class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict of {n -> index}
        d = {}
        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in d.keys():
                return [d[candidate], i]
            else:
                d[nums[i]] = i
        return []
