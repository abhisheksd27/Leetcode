from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        elif len(s) == k:
            return True
        else:
            a = Counter(s)
            cntodd = 0
            for i in a.values():
                if i % 2 != 0:
                    cntodd += 1
            if cntodd > k:
                return False
            return True