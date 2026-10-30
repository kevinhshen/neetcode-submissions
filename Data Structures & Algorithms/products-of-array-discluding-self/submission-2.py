class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        #      [1,2,3,4,5,6]
        # Pre: [1,2,6,24,120,720]
        # Post:[720,720,360,120,30,6]

        pointer = 0
        pre, post =[1]*len(nums),[1]*len(nums)
        pre[0]=nums[0]
        post[-1] = nums[-1]

        i=1
        while i < len(nums):
            pre[i] = nums[i]* pre[i-1]
            post[-i-1] = nums[-i-1] * post[-i]
            i+=1

        # print(f"Pre: {pre}, Post: {post}")
        
        nums[0] = post[1]
        nums[-1] = pre[-2]
        for i in range(1,len(nums)-1):
            nums[i] = pre[i-1] * post[i+1]

        

        return nums