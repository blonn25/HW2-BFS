# write tests for bfs
import pytest
from search import graph
import networkx as nx


def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    # initialize a Graph with 'tiny_network.adjlist'
    G = graph.Graph('data/tiny_network.adjlist')

    ### Unit Test 1 - Correct BFS Traversal Order ###    

    # traverse the graph starting with 'Hani Goodarzi'
    visited = G.bfs('Hani Goodarzi', end=None)

    # assert that the traversal yields the expected results in the expected order
    assert len(visited) == 30               # assert that the traversal visits all 30 nodes
    assert visited[0] == 'Hani Goodarzi'    # assert that the first node is 'Hani Goodrazi'
    assert visited[1] == '33232663'         # assert that the next visited node is '33232663'
    assert visited[2] in ['Charles Chiu', 'Martin Kampmann']  # assert that 3rd node visited is either 'Charles Chiu' or 'Martin Kampmann'
    assert visited[3] in ['Charles Chiu', 'Martin Kampmann']  # assert that 4th node visited is either 'Charles Chiu' or 'Martin Kampmann'

    ### Unit Tests 2 (Edge Case) - ValueError is Thrown When Start Node Does Not Exist ###

    # assert that a ValueError is thrown if the start input node does not exist in the graph
    with pytest.raises(ValueError):
        _ = G.bfs('foo', end=None)
    
    ### Unit Test 3 (Edge Case) - ValueError is Thrown When the Graph is Empty ###

    # set the current graph of G to an empty DiGraph
    G.graph = nx.DiGraph()

    # assert that a ValueError is thrown when the current graph is empty
    with pytest.raises(ValueError):
        _ = G.bfs('foo', end=None)


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    
    # initialize a Graph with 'citation_network.adjlist'
    G = graph.Graph('data/citation_network.adjlist')

    ### Unit Test 1 - Correct BFS for Connected Nodes ###    

    # search for the the shortest path from 'Hani Goodarzi' to 'Martin Kampmann'
    path = G.bfs('Hani Goodarzi', end='Luke Gilbert')

    # assert that the search yields a shortest path
    assert path is not None
    assert len(path) == 3
    assert path[0] == 'Hani Goodarzi'
    assert path[-1] == 'Luke Gilbert'

    ### Unit Test 2 - Correct BFS for Unconnected Nodes ###

    # search for the shortest path between '34850641' and 'Luke Gilbert' (there isn't one)
    no_path = G.bfs('34850641', end='Luke Gilbert')

    # assert that the search does not yield a path and returns None
    assert no_path == None

    ### Unit Tests 3-5 (Edge Cases) - ValueError is Thrown When Start and/or End Nodes Do Not Exist ###

    # assert that a ValueError is thrown if the start and/or end input nodes do not exist in the graph
    with pytest.raises(ValueError):
        _ = G.bfs('foo', end='Luke Gilbert')

    with pytest.raises(ValueError):
        _ = G.bfs('Hani Goodarzi', end='bar')
    
    with pytest.raises(ValueError):
        _ = G.bfs('foo', end='bar')

    ### Unit Test 6 (Edge Case) - ValueError is Thrown When the Graph is Empty ###

    # set the current graph of G to an empty DiGraph
    G.graph = nx.DiGraph()

    # assert that a ValueError is thrown when the current graph is empty
    with pytest.raises(ValueError):
        _ = G.bfs('foo', end='bar')