class Solution:
    def addDigits(self, num: int) -> int:
        
        stringed_ans = str(num)

        while len(stringed_ans) > 1:
            curr = 0
            for i in range(len(stringed_ans)):
                curr += int(stringed_ans[i])
            stringed_ans = str(curr)


        return int(stringed_ans)