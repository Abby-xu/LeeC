class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans,temp = -float('INF'),-1
        n=len(seats)
        for i in range(n):
            if seats[i]==0:
                pass
            else:
                if temp==-1: #if left most index is 0
                    ans=i
                else:
                    ans=max(ans,(i-temp)//2) #optimising the answer
                temp=i
        ans=max(ans,n-1-temp) #if right most index is 0
        return ans
