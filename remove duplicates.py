class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)

        #iteraton Case
        i = 0  #slow-run pointer
        for j in range(1, len(nums)):
            if nums[j] == nums[i]: 
                continue 
            if nums[j] != nums[i]: #capture the result
                i += 1
                nums[i] = nums[j] #in place overriden 
        return i + 1
            
