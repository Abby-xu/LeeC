class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(room: int) -> None:
            if room not in visited: 
                visited.add(room)
                for key in rooms[room]:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)
