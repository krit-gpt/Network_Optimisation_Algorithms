# Network Optimisation

The project deals with the **Maximum Bandwidth Path Problem.**
The project implements a network routing protocol using data structures and algorithms. Working on the problem of the Maximum-Bandwidth-Path Problem and having implemented three algorithms, namely: 
- Modified Dijkstra’s Algorithm 
- Modified Dijkstra’s Algorithm using a heap structure for fringes 
-  Modified Kruskal's Algorithm



The report discusses the implementation and the results of the implementation of these three  algorithms on two types of graphs:  
- **Sparse Graph** – Graph with 5000 vertices. The average vertex degree is 8. The graph edges have been assigned random positive weights.  
- **Dense Graph** – Graph with 5000 vertices. Each vertex is adjacent to about 20% of the other vertices, which are randomly chosen, which means that each vertex is connected to an approximate 1000 other vertices. The edges have been assigned random positive weights.  In the process of the implementation, I created various other data structures, such as:  
- **Max – Heap** – needed for modified Dijkstra’s Algorithm. 
- **Set (Union – Find)** – needed for modified Kruskal’s Algorithm.  
The results are stored in the results.xlsx file, and the attached project report discusses the results in details.

### How to run
1. Go into the src directory.
2. Select the .py file corresponding to the algorithm.
3. The graph is generated in the script only, depending on whether it is the dense or the sparse graph.
4. Run time of the algorithm will be the output.

(Rather than running the entire the project simultaneously, I have divided it into different files, with each having 
the complete code and the functionalities. Simple said, each script file is complete in itself, so that each piece can be a part of something bigger if one desires and wishes to take the project further for getting more insights into the problem.)

### About the Maximum Bandwidth Path Problem

**Maximum Bandwidth path problem:**  Given a source node 's' and a destination
node 't' in a network G, in which each edge 'e' is associated with a value
w(e), construct a path from 's' to 't' in G whose bandwidth is maximized (the
bandwidth of a path is equal to the minimum edge bandwidth over all edges in
the path).