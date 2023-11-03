class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def BS(num,arr):
            left =0
            right = len(arr)
            while right > left:
                mid=(right+left)//2
                if arr[mid] < num:
                    left = mid + 1
                else:
                    right=mid
            return left
        N  = len(nums)
        ans = [nums[0]]
        count = 1
        for i in range(1,N):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
                count +=1
            else:
                idx = BS(nums[i],ans)
                ans[idx] = nums[i]
        return count

        