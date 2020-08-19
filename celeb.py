def naive_topsort(G,S=None):
    if S is None: S= set(G)
    if len(S) ==1: return list(S)
    v= S.pop()
    seq = naive_topsort(G,S)
    min_i = 0
    for i,u in enumerate(seq):
        if v in G[u]: min_i += 1
    seq.insert(min_i, v)
    return seq


G = [
    [0,1,0,0,0,1],
    [0,0,1,1,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0]
    ]

naive_topsort(G)