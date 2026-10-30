class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        #      [1,2,3,4,5,6]
        # Pre: [1,2,6,24,120,720]
        # Post:[720,720,360,120,30,6]

        
        out = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]


        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] *= postfix
            postfix *= nums[i] 
        

    
        

        return out