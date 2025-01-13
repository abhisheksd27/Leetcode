class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [0] * 26
        len = 0
        
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
            
        for num in cnt:
            if num == 0:
                continue
            len += 2 if num % 2 == 0 else 1
            
        return len