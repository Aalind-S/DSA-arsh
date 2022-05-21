class Solution:
    from heapq import heappop, heappush
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            distance = -1*( points[i][0]**2 + points[i][1]**2 )
            heappush(res, (distance, i))
            if len(res) > k:
                heappop(res)
        
        return [points[y] for x, y in res]
        
