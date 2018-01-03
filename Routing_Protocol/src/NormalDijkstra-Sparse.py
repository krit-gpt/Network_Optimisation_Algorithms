from collections import defaultdict
import sys
import random
from random import randint
import timeit

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        node = [v,w]
        self.graph[u].append(node)

        node2 = [u,w]
        self.graph[v].append(node2)


    def Dijkstra(self, s, t):
        status = []
        dad =[ ]
        bw = [ ]

        for v in range(self.V):
            status.append('unseen')
            dad.append(None)
            bw.append(-sys.maxsize)
        #print(status)
        #print(dad)
        #print(bw)

        status[s] = 'in-tree'


        for pCrawl in self.graph[s]:
            v = pCrawl[0]
            w = pCrawl[1]
            status[v] = 'fringe'
            dad[v] = s
            bw[v] = w
        #print(status)
        #print(dad)
        #print(bw)

        while status[t] != 'in-tree':
            #print(bw)
            index_max_fringe = bw.index(max(bw))
            v_bw = bw[index_max_fringe]
            bw[index_max_fringe] = (-sys.maxsize)

            status[index_max_fringe] = 'in-tree'
            #print(status)
            #print(bw)

            for pCrawl in self.graph[index_max_fringe]:
                w = pCrawl[0]
                weight = pCrawl[1]

                #print(w, "+", weight)

                if status[w] == 'unseen':
                    status[w] = 'fringe'
                    dad[w] = index_max_fringe
                    bw[w] = min(v_bw, weight)
                    #print(status)

                elif status[w] == 'fringe' and bw[w] < min(v_bw, weight):
                    bw[w] = min(v_bw, weight)
                    dad[w] = index_max_fringe
                    #print(status)


        print(dad)
        print(status)
        #print(bw)


        # print(max_fringe)
        # print(index_max_fringe)
        # print(bw)


################ ------------------ RANDOM GRAPH ------------------------ ####################

# g = Graph(100)
#
#
# for i in range(0,99):
#     g.addEdge(i, i+1, randint(1,100))
#
# g.addEdge(99, 0, 20)
#
# for i in range(0,99):  #for each 100 vertices
#     randvertex = random.sample(range(1,98), 6)  # Generating 6 random vertices
#
#     for ele in randvertex:
#         if ele != i:
#             g.addEdge(i, ele, randint(1,100))
#         else:
#             g.addEdge(i, randint(20,50), randint(1,100))
#
#
#
# g.Dijkstra(0,10)


def main():

    g = Graph(5000)

    '''
    Generating a cycle so as to ensure that the graph is connected

    '''

    for i in range(0,4999):
        g.addEdge(i, i+1, randint(1,1000))

    g.addEdge(4999, 0, 20)

    for i in range(0,4999):  #for each 5000 vertices
        randvertex = random.sample(range(1,4990), 6)  # Generating 6 random vertices which are unique to avoid multiple edges

        for ele in randvertex:
            if ele != i:                               # Making sure that a self edge is not made by the graph
                g.addEdge(i, ele, randint(1,5000))
            else:
                g.addEdge(i, randint(2000,4900), randint(1,1000))


    start =timeit.default_timer()
    g.Dijkstra(randint(1,4999),randint(1,4999))
    stop = timeit.default_timer()
    print(round(stop-start, 6), "Seconds")

if __name__ == "__main__":
    main()