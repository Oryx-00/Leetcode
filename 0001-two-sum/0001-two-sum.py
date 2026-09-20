class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return (hash_map[complement], index)
            hash_map[num] = index
        