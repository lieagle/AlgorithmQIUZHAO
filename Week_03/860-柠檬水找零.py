#Leetcode 860

#解法一、时间复杂度：O(n),空间O(1).n是bills长度。
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else: return False
        return True


#C++版本
class Solution{
    public:
    bool lemonadeChange(vector<int>& bills){
        int five = 0;
        int ten = 0;
        int len = bills.size();
        for (int i = 0; i < len; ++ i){
            if (bills[i] == 5){
                five++;
            }
            else if (bills[i] == 10){
                ten++;
                five--;
            }
            else if (bills[i] == 20){
                if (ten > 0){
                    ten--;
                    five--;
                }
                else{
                    five -= 3;
                }
            if (five < 0){
                return false;
            }
            }

        }
        return true;
    }
};