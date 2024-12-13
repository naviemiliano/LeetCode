class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1
        
        rawr = []
        
        for num in nums:
            if num not in rawr and num != 0:
                rawr.append(num)
                print (rawr)
                
        return len(rawr)
