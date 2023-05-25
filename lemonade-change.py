class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twen = 0

        for bill in bills:
            if bill==5:
                five += 1
            elif bill==10:
                if five < 1:
                    return False
                else:
                    five -= 1
                ten += 1
            else:
                if ten > 0:
                    ten -= 1
                    if five > 0:
                        five -= 1
                    else:
                        return False
                else:
                    if five > 2:
                        five -= 3
                    else:
                        return False
        return True