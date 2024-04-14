### Count frequencies
- suppose req = [[1,3],[0,1]]
- you have to find out the frequencies of numbers in ranges
```
pre = [0 for i in range(n)]
for s,e in req:
    pre[s] += 1
    if e+1 < n:
        pre[e+1] += -1
for i in range(1,n):
    pre[i] += pre[i-1]
```
