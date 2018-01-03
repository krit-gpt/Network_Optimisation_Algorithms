from collections import defaultdict
import sys
import timeit
import random
from random import randint




class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMaxHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # A utility function to swap two nodes
    # of min heap. Needed for min heapify
    def swapMaxHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def maxHeapify(self, idx):
        smallest = idx
        #print("smallest is ", smallest)
        left = 2*idx + 1
        right = 2*idx + 2


        if right < self.size :
            if self.array[right][1] > self.array[left][1]:
                max = right
            else:
                max = left

            if self.array[max][1] > self.array[smallest][1]:
                smallest = max

        elif left < self.size:
            if self.array[left][1] > self.array[smallest][1]:
                smallest = left




        # if right < self.size and self.array[right][1] \
        #         > self.array[smallest][1]:
        #     smallest = right
        #
        # elif left < self.size and self.array[left][1] \
        #         > self.array[smallest][1]:
        #     smallest = left

        # The nodes to be swapped in min
        # heap if idx is not smallest
        if smallest != idx:

            # Swap positions
            self.pos[ self.array[smallest][0] ] = idx
            self.pos[ self.array[idx][0] ] = smallest

            #print("array before swap is ", self.array)

            # Swap nodes
            self.swapMaxHeapNode(smallest, idx)

            self.maxHeapify(smallest)
            self.maxHeapify(0)


    def extractMax(self):

        # Return NULL if heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1


        self.size -= 1
        self.maxHeapify(0)
        #print("root is ", root)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):



        i = self.pos[v]

        self.array[i][1] = dist

        while (i > 0 and self.array[i][1] > self.array[(i - 1) // 2][1]):

            # Swap this node with its parent
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swapMaxHeapNode(i, (i - 1) // 2)

            i = (i - 1) // 2

    def isInMaxHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)


    def addEdge(self, src, dest, weight):


        newNode = [dest, weight]
        self.graph[src].append (newNode)


        newNode2 = [src, weight]
        self.graph[dest].append(newNode2)

    def dijkstra(self, src, t):

        V = self.V # Get the number of vertices in graph
        dist = [] # dist values used to pick minimum
        # weight edge in cut
        status = []
        dad = []

        # maxHeap represents set E
        maxHeap = Heap()

        for v in range(V):
            status.append('unseen')
            dist.append(-sys.maxsize)
            dad.append(None)

        status[src] = 'in-tree'

        for pCrawl in self.graph[src]:
            v = pCrawl[0]
            w = pCrawl[1]
            status[v] = 'fringe'
            dad[v] = src
            dist[v] = w


        for v in range(V):
            #dist.append(sys.maxsize)
            maxHeap.array.append(maxHeap.newMaxHeapNode(v, dist[v]))
            maxHeap.pos.append(v)
            maxHeap.maxHeapify(0)

        maxHeap.size = V;


        while status[t] != 'in-tree':

            # Extract the vertex with minimum distance value
            newHeapNode = maxHeap.extractMax()
            u = newHeapNode[0]


            status[u] = 'in-tree'

            for pCrawl in self.graph[u]:

                v = pCrawl[0]
                weight = pCrawl[1]

                if status[v] == 'unseen':
                    status[v] = 'fringe'
                    dad[v] = u
                    dist[v] = min(dist[u],weight)
                    maxHeap.decreaseKey(v, dist[v])

                elif status[v] == 'fringe' and dist[v] < min(dist[u],weight):
                    maxHeap.decreaseKey(v, dist[v])
                    dist[v] = min(dist[u], weight)
                    dad[v] = u
                    maxHeap.decreaseKey(v, dist[v])



        print(status)
        print(dist)
        print(dad)



#
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
    g.dijkstra(randint(1,999),randint(1999,4999))
    stop = timeit.default_timer()
    print(round(stop-start, 6), "Seconds")
    print("-----------------------------------------------")

if __name__ == "__main__":
    main()