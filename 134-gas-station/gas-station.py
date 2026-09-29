class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = 0
        total_cost = 0

        for val in gas:
            total_gas += val
        for val in cost:
            total_cost += val
        
        if(total_gas < total_cost):
            return -1
    
        start = 0
        currGas = 0

        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if(currGas < 0):
                start = i + 1
                currGas = 0
        
        return start