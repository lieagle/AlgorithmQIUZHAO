#用到哈希表
#arr1元素按照个数与元素对的形式存储在哈希表中，
#把arr1中不在arr2中的元素都存到not_in_arr2里;
#把arr1中剩余和arr2中一样的元素都存到in_arr2里
#返回in_arr2 + not_in_arr2即可
#arr1按照arr2为关键字排序

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        in_arr2 = []
        not_in_arr2 = []
        Hash = {}
        for i in arr1:
            Hash[i] = Hash.get(i, 0) + 1
        arr1 = set(arr1)
        for j in arr1:
            if j not in arr2:
                not_in_arr2 += [j] * Hash[j]
        not_in_arr2.sort()
        for k in arr2:
            in_arr2 += [k] * Hash[k]
        return in_arr2 + not_in_arr2
