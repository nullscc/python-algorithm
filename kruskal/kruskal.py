"""
kruskal算法
"""

from math import inf
from operator import itemgetter

def gen_edges(gragh):
    data = []
    d = {}
    for i, l in enumerate(gragh):
        for j, _ in enumerate(l):
            if gragh[i][j] == 0 or gragh[i][j] == inf:
                continue
            if d.get(j) and i in d.get(j):
                continue
            temp = {}
            temp["begin"] = i
            temp["end"] = j
            temp["weight"] = gragh[i][j]
            data.append(temp)
            d.setdefault(i, [])
            d[i].append(j)
    data.sort(key=itemgetter("weight"))
    return data

def find(parent, f):
    while (parent[f] > 0):
        f = parent[f]
    return f

def print_mini_span_tree(gragh):
    # 为了方便这里直接用邻接矩阵生成了~~
    edges = gen_edges(gragh)
    parent = []

    for i in range(len(gragh)):
        parent.append(0)

    for d in edges:
        n = find(parent, d["begin"])
        m = find(parent, d["end"])
        if n != m:
            parent[n] = m
            print("({}, {}) {}".format(d["begin"], d["end"], d["weight"]))

if __name__ == "__main__":
    gragh = [
        [0, 10, inf, inf, inf, 11, inf, inf, inf],
        [10, 0, 18, inf, inf, inf, 16, inf, 12],
        [inf, inf, 0, 22, inf, inf, inf, inf, 8],
        [inf, inf, 22, 0, 20, inf, 24, 16, 21],
        [inf, inf, inf, 20, 0, 26, inf, 7, inf],
        [11, inf, inf, inf, 26, 0, 17, inf, inf],
        [inf, 16, inf, inf, inf, 17, 0, 19, inf],
        [inf, inf, inf, 16, 7, inf, 19, 0, inf],
        [inf, 12, 8, 21, inf, inf, inf, inf, 0]
    ]

    print_mini_span_tree(gragh)
