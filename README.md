![BuildStatus](https://github.com/blonn25/HW2-BFS/actions/workflows/test.yml/badge.svg?event=push)

# Assignment 2: Breadth-First Search
Breadth-first search (BFS) is an algorithm for traversing graphs which starts from a user-defined source node and explores new nodes "layer-by-layer." To achieve this, BFS leverages a queue system. Beginning with the source node, each neighbor is explored and pushed into the queue. With each successive cycle, the node at the front of the queue is popped; then any of its neighbors which have not been previously explored are pushed into the queue. This cycle continues until the entirety of the graph has been traversed. Notably, BFS can also be used to find a shortest path between a user-defined source and end node in an unweighted graph.
