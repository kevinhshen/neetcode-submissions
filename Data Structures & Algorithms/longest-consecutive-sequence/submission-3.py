class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start=[]
        max_sequence: int = 0

        for i in nums_set:
            if i-1 not in nums_set:
                cur_sequence = 0

                while i + cur_sequence in nums_set:
                    cur_sequence+=1

                max_sequence = max(max_sequence,cur_sequence)
                
        return max_sequence