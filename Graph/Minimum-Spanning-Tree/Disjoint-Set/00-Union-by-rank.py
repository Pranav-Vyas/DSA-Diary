'''
--------------  Union by rank and path compression  ----------------
'''

# vertices = v

def union_by_rank(n, edges):
  rank = [0 for _ in range(n)]
  parent = [i for i in range(n)]

  def find(u):
    if u != parent[u]:
      parent[u] = find(parent[u])
    return parent[u]
  
  def union(u,v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
      return
    if rank[pu] > rank[pv]:
      parent[pv] = pu
    if rank[pu] < rank[pv]:
      parent[pu] = pv
    else:
      parent[pv] = pu
      rank[pu] += 1
  
# This technique is used for dynamically changing graph.
# At any point of time during addition of edges, 
# we can determine if two nodes are in same component by checking their parents