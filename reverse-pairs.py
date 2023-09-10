class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        def reverse(left_arr,right_arr):
            if not left_arr or not right_arr:
                return
            for n in left_arr:
                self.count += bisect.bisect_left(right_arr,ceil(n/2))
            
            res = []
            l = r = 0
            L = len(left_arr)
            R = len(right_arr)

            while l < L and r < R:
                if left_arr[l] <= right_arr[r]:
                    res.append(left_arr[l])
                    l+=1
                else:
                    res.append(right_arr[r])
                    r+=1
            
            while r < R:
                res.append(right_arr[r])
                r+=1
            while l < L:
                res.append(left_arr[l])
                l+=1
        
            return res


            

        def divide(left, right):
            if left==right:
                return [nums[left]]
            
            mid = left + (right-left)//2

            left_half = divide(left, mid)
            right_half = divide(mid+1, right)
            return reverse(left_half, right_half)

        divide(0,len(nums)-1)

        return self.count
        # print(bisect.bisect_right([1,3],3))