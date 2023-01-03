import heapq
h=[10,23,8,39,14]
heapq.heapify(h)
print(h)
heapq.heappop(h)
print(h)
heapq.heappush(h,25)
print(h)
heapq.heapreplace(h,6)
print(h)
heapq.heappushpop(h,99)
print(h)