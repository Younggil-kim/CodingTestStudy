class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                result.append(nums[i] + nums[j])
                if target in result:
                    return [i,j]
