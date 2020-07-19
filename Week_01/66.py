#leetcode 66.Plus One
#将列表转换为整数num。 因此，每个数字都乘以适当的位置值，然后加到num上。
#数字加1，然后转换成列表返回。
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]












