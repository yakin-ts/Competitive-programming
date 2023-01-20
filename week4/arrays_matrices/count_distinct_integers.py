class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        leng = len(nums)
        unique = {}
        count_unique = 0
        
        for i in range (leng):
            new_int = str(nums[i])
            nums.append(int(new_int[::-1]))
            
        for i, num in enumerate(nums):
            if num not in unique:
                unique[num] = 1
                count_unique +=1
        
        return count_unique