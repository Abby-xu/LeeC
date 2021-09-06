class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        index, self.longest = 0, releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i]-releaseTimes[i-1] > self.longest:
                index = i
                self.longest = releaseTimes[i]-releaseTimes[i-1]
            if releaseTimes[i]-releaseTimes[i-1] == self.longest and keysPressed[index] < keysPressed[i]:
                index = i
        return keysPressed[index]
