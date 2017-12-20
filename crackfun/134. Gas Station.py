# BLE version
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)
        for i in range(N):
            res = [gas[i]-cost[i]]
            for j in range(i+1, i+N+1):
                res.append(res[-1]+gas[j%N]-cost[j%N])
            if min(res)>=0:
                return i
        else:
            return -1

# AC solution
 class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalgas = 0
        totalcost = 0
        start = 0
        balance = 0
        for i in xrange(0, len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0
        if totalcost <= totalgas:
            return start
        return -1