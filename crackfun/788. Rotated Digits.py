class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {0:0,1:1,8:8,2:5,5:2,6:9,9:6}
        cnt = 0
        for num in range(1,N+1):
            oldnum = num
            rnum = 0
            flag = 0
            while num:
                if num%10 in d:
                    rnum=rnum*10 + d[num%10]
                    num//=10
                else:
                    flag = 1
                    break
            if not flag and rnum!=oldnum:
                print(oldnum)
                cnt+=1

        return cnt