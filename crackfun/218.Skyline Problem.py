class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    import heapq
    def getSkyline(self, buildings):
        idx, n = 0, len(buildings)
        liveBuildings, skyline = [], []
        while idx < n or len(liveBuildings) > 0:
            if len(liveBuildings) == 0 or (idx < n and buildings[idx][0] <= -liveBuildings[0][1]):
                start = buildings[idx][0]
                while idx < n and buildings[idx][0] == start:
                    heapq.heappush(liveBuildings, [-buildings[idx][2], -buildings[idx][1]])
                    print(heapq)
                    idx += 1
            else:
                start = -liveBuildings[0][1]
                while len(liveBuildings) > 0 and -liveBuildings[0][1] <= start:
                    heapq.heappop(liveBuildings)
            height = len(liveBuildings) and -liveBuildings[0][0]
            if len(skyline) == 0 or skyline[-1][1] != height:
                skyline.append([start, height])

        return skyline

    import heapq
    # This is a TLE version
    def getSkyline2(self, buildings):
        res = []
        heights = []
        liveheights = []
        for idx in range(len(buildings)):
            heights.append((buildings[idx][0], -buildings[idx][2]))
            heights.append((buildings[idx][1], buildings[idx][2]))
        heights.sort(key = lambda x:(x[0], x[1]))  # This sort based on two attributes will guarantee to have start first and end point later

        prev = 0
        liveheights = [0]
        for x in heights:
            if x[1]<0: # start point
                heapq.heappush(liveheights, -x[1])
            else:
                liveheights.remove(x[1])
                heapq.heapify(liveheights)
            curr = heapq.nlargest(1, liveheights)[0]
            if prev!=curr:
                res.append([x[0],curr])
                prev = curr
        return res
