
#75.
6.两次遍历
第一次统计每个颜色出现次数
第二次遍历将数组重新赋值
时间复杂度：O（m*n），m为颜色个数，
n为数组长度，需要遍历两次数组。m=3,也是O(N)

空间复杂度：O（m），需要新建一个长度为m的一维数组。
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color = [0]*3
        for i in nums:
            color[i] += 1
        j = 0
        for m in range(3):
            for n in range(color[m]):
                nums[j] = m
                j += 1




#7.最佳：一次遍历，三指针法，时间O(n),空间：O(1)

   #三指针，把0往前放，2最后放，1不管
        #i 用于保存先前的1的位置，等找到0时候再2把0换过来
        i=0
        #当左指针为0，把先前的1换掉；当左指针为2时，放到最右边去，然后右指针往左走，继续判断，直至满足条件。
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]==0:
                nums[l],nums[i]=nums[i],nums[l]
                i+=1
                l+=1
            elif nums[l]==2:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            else:
                l+=1
        return nums





#1.冒泡排序：是从头开始比较，相邻数据两两比较，如果前一个更大，则交换。
#不断重复这个交换过程，直到排序完成。通过交换元素逐步消除逆序
#时间复杂度O(n^2),空间复杂度O(1)，稳定排序（相同元素不改变相对位置）

#2.快速排序，快速排序分为三步：
1.选择一个标准，根据这个标准，这组数据被划分为2份，小的那份在前
2.递归实现继续划分，在已经划分好的两份里面继续执行（1）
3.每个数据成为一组时，划分完毕
时间复杂度O(nlogn)，空间复杂度O(logn)，不稳定



3.选择排序
这种方法和我们正常的思维很像，依次找到最小的，次小的... 然后放在第一位，第二位...
即：1.找到数据中最小的放在首位；2.在剩余数据中找到最小的放在第二位；3.直到全部放置完毕
时间复杂度O(n^2),空间复杂度O(1)，不稳定


4.插入排序
是一种稳定排序，每次抽出一个未排序的数字和前面已排序的数组中数据进行比较，如果比每个都大，则放在已排序的数组后面，否则比该未排序的数字大的已排序的数组中数据后移一位。
1.插入前和已排好序的数值比较
2.若大于该数值，则继续往后遍历，直到遍历全部已排序数组
3，若小于该数值，则插入到该数值前面一位，该数及后续数后移一位
时间复杂度O(n^2),空间复杂度O(1)，不稳定

5.归并排序
归并排序就是分治思想的强力体现了。
思路是：（感觉和快排有点相反的味道）
首先将原始数组中看做n个有序的子数组，然后两两合并，合并完成后保持合并后的子数组仍有序，再不断两两合并，直到得到长度为n的有序数组
时间复杂度O(nlogn)，空间复杂度O(n)，稳定



