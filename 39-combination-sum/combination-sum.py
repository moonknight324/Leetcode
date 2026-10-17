class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        def backtrack(curr_comb,remaining_t,start_index):
            if remaining_t == 0:
                result.append(list(curr_comb))
                return
            if remaining_t<0:
                return
            for i in range(start_index,len(candidates)):
                curr_comb.append(candidates[i])
                backtrack(curr_comb,remaining_t-candidates[i],i)
                curr_comb.pop()
        
        backtrack([],target,0)
        return result