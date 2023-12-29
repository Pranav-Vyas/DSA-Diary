'''
--------------  Union by rank and path compression  ----------------
'''

# vertices = v

def union_by_size(v, edges):
  size = [0 for _ in range(v)]
  parent = [i for i in range(v)]

  def find(u):
    if u != parent[u]:
      parent[u] = find(parent[u])
    return parent[u]
  
  def union(u,v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
      return
    if size[pu] > size[pv]:
      parent[pv] = pu
      size[pu] += size[pv]
    if size[pu] < size[pv]:
      parent[pu] = pv
      size[pv] += size[pu]
    else:
      parent[pv] = pu
      size[pu] += size[pv]