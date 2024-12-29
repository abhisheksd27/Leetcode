class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # h={}
        # for i in nums:
        #     if i not in h:
        #         h[i]=1
        #     else:
        #         return True
        # return False


        return len(set(nums))<len(nums)
        