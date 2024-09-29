import pandas as pd


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist, P, T):
        d = {}
        for node in range(self.V):
            d[chr(ord('A') + node)] = [T[node], dist[node] if dist[node] != 1e7 else '\u221E', P[node]]
        print("_____________________________________________________")
        df = pd.DataFrame(d)
        print(df.to_string(index=False))
        print("\n")

    def minDistance(self, dist, sptSet):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        P = ["_"] * self.V
        T = ["_"] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            T[u] = chr(ord('A') + u)
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    P[v] = str(chr(ord('A') + u))
                    dist[v] = dist[u] + self.graph[u][v]
            self.printSolution(dist, P, T)


# g = Graph(8)
#         #   A  B  C  D  E  F  G  H
# g.graph = [[0, 7, 2, 0, 0, 5, 0, 0],
#            [7, 0, 0, 4, 3, 0, 0, 0],
#            [2, 0, 0, 0, 7, 0, 0, 4],
#            [0, 4, 0, 0, 0, 3, 5, 0],
#            [0, 3, 7, 0, 0, 0, 4, 0],
#            [5, 0, 0, 3, 0, 0, 0, 3],
#            [0, 0, 0, 5, 4, 0, 0, 5],
#            [0, 0, 4, 0, 0, 3, 5, 0]
#            ]

graph = [[0, 3, 1, 0, 0],
         [3, 0, 7, 5, 1],
         [1, 7, 0, 2, 0],
         [0, 5, 2, 0, 7],
         [0, 2, 0, 7, 0]
        ]

g = Graph(len(graph))
g.graph = graph
g.dijkstra(0)