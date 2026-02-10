class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        
        for i, num in enumerate(nums):
            needed = target - num
            
            if needed in index_map:
                return [index_map[needed], i]
            
            index_map[num] = i
