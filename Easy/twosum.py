class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,values in enumerate(nums):
            integerneeded=target-values
            if integerneeded in dict:
                return [dict[integerneeded],i]
            dict[values]=i