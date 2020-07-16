class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        gasNeeded = 0
        gasLeft = 0
        end = -1

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            if gasLeft + diff < 0:
                ## restart here
                gasNeeded -= gasLeft + diff
                end = i
                gasLeft = 0
            else:
                gasLeft += diff
        
        return (end + 1) % len(gas) if gasLeft >= gasNeeded else -1

s = Solution()

gas  = [1,2,7,4,5]
cost = [3,4,4,1,2]

gas = [1]
cost = [1]

print(s.canCompleteCircuit(gas, cost))
        