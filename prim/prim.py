"""
prim算法：
1. 选定一个起点
2. 找到与起点相连的最小权值的边
3. 找到与第2步中的边相连且没有处理过的点的最小权值的边
4. 重复2-3，直到所有点都处理过
"""

from math import inf

def print_mini_span_tree(gragh):
    # 最小代价数组，存储的始终是当前与已经找到的点/边之间最小代价的点的权值，通过遍历过程的赋值来保证这点
    # 如果下标对应的值为0，说明已经处理过了
    lowcost = []

    # 当根据lowcost找到最小代价的坐标ｋ,需要根据此列表中的值来找到与ｋ坐标连线的那个点
    adjvex = []

    # 这里找到与起点相连的所有的边
    for i in range(len(gragh)):
        lowcost.append(gragh[0][i])
        adjvex.append(0)

    for i in range(1, len(gragh)):
        min_weight = inf
        k = 0

        # 遍历一次就能找到一个与已经形成的边相连的且权值最小的边
        for j in range(1, len(gragh)):
            if (lowcost[j] != 0) and lowcost[j] < min_weight:
                min_weight = lowcost[j]
                k = j

        print("{}, {}".format(adjvex[k], k))

        lowcost[k] = 0

        # 这里是为了将与已经找到的边相连的边相关的权值与起始点存入数据，以便在下次循环中使用
        for j in range(1, len(gragh)):
            if lowcost[j] != 0 and gragh[k][j] < lowcost[j]:
                lowcost[j] = gragh[k][j]
                adjvex[j] = k

if __name__ == "__main__":
    gragh = [
        [0, 10, inf, inf, inf, 11, inf, inf, inf],
        [10, 0, 18, inf, inf, inf, 16, inf, 12],
        [inf, inf, 0, 22, inf, inf, inf, inf, 8],
        [inf, inf, 22, 0, 20, inf, inf, 16, 21],
        [inf, inf, inf, 20, 0, 26, inf, 7, inf],
        [11, inf, inf, inf, 26, 0, 17, inf, inf],
        [inf, 16, inf, inf, inf, 17, 0, 19, inf],
        [inf, inf, inf, 16, 7, inf, 19, 0, inf],
        [inf, 12, 8, 21, inf, inf, inf, inf, 0]
    ]

    print_mini_span_tree(gragh)
