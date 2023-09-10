class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        dic_x = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        sorted_dic=dict(dic_x)
        top_k = []
        count = 0
        for item in sorted_dic.keys():
            if count==k:
                break
            else:
                top_k.append(item)
                count +=1
        return top_k