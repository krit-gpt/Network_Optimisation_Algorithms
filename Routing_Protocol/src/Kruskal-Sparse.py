'''Header Files to be used in the program'''
from collections import defaultdict
import random
from random import randint
import timeit

'''Global variable made which will have the results - that is the Maximum Spanning Tree '''

resultss = []



class Graph2:

    '''Constructor for the class
        addEdge2( ) adds an edge to the class'''
    def __init__(self):
        self.graph2 = defaultdict(list)

    def addEdge2(self,u,v):
        self.graph2[u].append(v)
        self.graph2[v].append(u)

    def Recur(self, v, visited, t, final_dfs):

        '''Modifiying DFS so that it returns when
        target vertex - t is reached'''

        if visited[t] == True:
            return

        visited[v] = True
        final_dfs.append(v)

        for i in self.graph2[v]:
            if visited[i] == False:
                self.Recur(i, visited, t, final_dfs)

    def DFS(self,v,t):

        final_dfs = [ ]

        visited = [False]*(len(self.graph2))
        self.Recur(v, visited, t, final_dfs)
        print(final_dfs)

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2


        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r


        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]  # swap


            self.heapify(arr, n, largest)

    # The main function to sort an array of given size
    def sorted(self, arr):
        n = len(arr)


        for i in range(n, -1, -1):
            self.heapify(arr, n, i)


        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        self.graph.append([v,u,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def getresultss(self):
        return resultss

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self,s,t):


        treee =[]

        i = 0
        e = 0

        time3 = timeit.default_timer()
        self.graph =  sorted(self.graph, key=lambda item: item[2], reverse = True)
        time4 = timeit.default_timer()

        print("---------------------------------")

        parent = [] ; rank = []

        # Create V Sets with single elements initially
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :

            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            if x != y:
                e = e + 1
                treee.append([u,v,w])
                self.union(parent, rank, x, y)

        global resultss
        resultss = treee



'''Main Function that drives the program'''


def main():
    g = Graph(5000)

    '''
    Generating a cycle so as to ensure that the graph is connected

    '''

    for i in range(0,4999):
        g.addEdge(i, i+1, randint(1,1000))

    g.addEdge(4999, 0, 20)

    for i in range(0,4999):  #for each 1000 vertices
        randvertex = random.sample(range(1,4990), 6)  # Generating 6 random vertices which are unique to avoid multiple edges

        for ele in randvertex:
            if ele != i:                               # Making sure that a self edge is not made by the graph
                g.addEdge(i, ele, randint(1,1000))
            else:
                g.addEdge(i, randint(20,4900), randint(1,1000))


    start =timeit.default_timer()
    g.KruskalMST(3,20)
    stop = timeit.default_timer()
    time1 = stop-start
    print(stop-start, "Seconds")

    print("_________________________________")
    print("The Dad Array[ ] starts here" )


    g1 = Graph2()
    for u,v,w in resultss:
        g1.addEdge2(u,v)

    s = randint(1,1999)
    t = randint(2000,4999)

    start2 =timeit.default_timer()
    g1.DFS(s,t)
    stop2 = timeit.default_timer()
    print(stop2-start2, "Seconds")
    time2 = stop2-start2

    print("Total time : ", round(time1+time2,6), "seconds")

if __name__ == "__main__":
    main()


