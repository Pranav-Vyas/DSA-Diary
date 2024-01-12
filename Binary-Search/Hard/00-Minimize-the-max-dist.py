# https://www.codingninjas.com/studio/problems/minimise-max-distance_7541449

''' Method 1 Heap'''

from heapq import *
def minimiseMaxDistance(arr: [int], k: int) -> float:
    pq = []
    n = len(arr)
    count = [1 for i in range(n-1)]
    for i in range(n-1):
        pq.append((-(arr[i+1] - arr[i]),i))
    heapify(pq)
    while k:
        diff,i = heappop(pq)
        diff = abs(diff)
        count[i] += 1
        diff = (arr[i+1] - arr[i])/count[i]
        heappush(pq, (-diff,i))
        k -= 1
    diff,i = heappop(pq)
    return abs(diff)

''' Method 2 Binary Search'''