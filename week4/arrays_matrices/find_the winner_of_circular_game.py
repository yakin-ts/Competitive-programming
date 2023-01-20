class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        def helper(circ,nxt,head):
            if len(circ)==1:
                return circ[-1]
            head = ((nxt+head)-1)%len(circ)
            circ.pop(head)
            return helper(circ,nxt,head)
        return helper(friends,k,0)