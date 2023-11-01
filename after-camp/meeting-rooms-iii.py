class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [i for i in range(n)]
        mem = [0 for _ in range(n)]
        occupied = []
        freq = 0
        heapq.heapify(rooms)
        most = n
        for x, y in meetings:
            while occupied and occupied[0][0] <= x:
                _, room_id = heapq.heappop(occupied)
                heapq.heappush(rooms,room_id)
            if rooms:
                room_id = heapq.heappop(rooms)
                heapq.heappush(occupied,[y,room_id])
            else:
                time, room_id = heapq.heappop(occupied)
                heapq.heappush(occupied,[y+time-x, room_id])
            mem[room_id] +=1

            if freq < mem[room_id]:
                freq = mem[room_id]
                most = room_id
        
            elif mem[room_id] == freq:
                most = min(most,room_id)
            
        return most


                    


