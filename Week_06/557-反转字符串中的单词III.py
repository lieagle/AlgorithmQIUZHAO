#先把字符串按单个字符全部反转；再按空格把每个单次分割；反转；拼接。
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s1 = s.split(' ')
        s1.reverse()
        return ' '.join(s1)



