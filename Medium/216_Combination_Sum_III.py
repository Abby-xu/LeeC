class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        allNumbers=[i for i in range(1,10)]
        res=[]
        for item in itertools.combinations(allNumbers,k):
            if sum(item)==n:
                res.append(item)
                
        return res    
