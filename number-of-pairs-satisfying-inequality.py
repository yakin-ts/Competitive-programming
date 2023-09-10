class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # divide
        # compare
        # sort
        # repeate
        self.diff = diff
        self.count = 0

        tmp = [nums1[i] + - nums2[i] for i in range(len(nums1))]

        def compare(left,right):
            if not left or not right:
                return
            j = 0
            while j < len(right):
                self.count += bisect.bisect_right(left,right[j]+self.diff)
                j+=1
            l = k = 0
            r = 0
            res = []
            while l < len(left) and  r < len(right):
                if left[l] <= right[r]:
                   res.append(left[l])
                   l += 1
                else:
                    res.append(right[r])
                    r += 1
            while l < len(left):
                res.append(left[l])
                l+=1
            while r < len(right):
                res.append(right[r])
                r+=1

            return res

        def divide(left, right):
            if left==right:
                return [tmp[left]]
            mid = left + (right-left)//2

            l_half = divide(left,mid)
            r_half = divide(mid+1,right)
            return compare(l_half,r_half)
        
        divide(0,len(nums1)-1)

        return self.count