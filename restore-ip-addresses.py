class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)

        def helper(idx, sect):
            if idx == len(s) and sect == 4:
                allIps.append(".".join(tempIps))
                return
            if sect >= 4:
                return

            for i in range(1, 4):
                if N >= idx + i:
                    part = s[idx: idx + i]
                    if 0 <= int(part) <= 255 and (len(part) == 1 or part[0] != '0'):
                        tempIps.append(part)
                        helper(idx + i, sect + 1)
                        tempIps.pop()

        allIps = []  
        tempIps = []
        helper(0, 0)
        return allIps