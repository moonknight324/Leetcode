class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = 0
        total_cost = 0
    
        start = 0
        currGas = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            currGas += gas[i] - cost[i]
            if(currGas < 0):
                start = i + 1
                currGas = 0
                
        if(total_gas < total_cost):
            return -1
        
        return start