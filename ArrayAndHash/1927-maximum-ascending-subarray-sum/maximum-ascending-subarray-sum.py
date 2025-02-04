class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0] 
        for a, b in pairwise(nums): 
            cur_sum = cur_sum + b if a < b else b 
            max_sum = max(max_sum, cur_sum) 
        return max_sum