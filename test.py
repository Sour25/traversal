import unittest
from collections import defaultdict, deque

# DFS and BFS implementations
def dfs(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
        traversal = []
    visited.add(start)
    traversal.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)
    return traversal

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal

# Unit tests
class TestGraphTraversal(unittest.TestCase):

    def setUp(self):
        # Sample graph for testing
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B'],
            'E': ['B'],
            'F': ['C'],
            'G': ['C']
        }
        self.disconnected_graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }

    def test_dfs(self):
        # Test DFS on connected graph
        result = dfs(self.graph, 'A')
        expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
        self.assertEqual(result, expected)

    def test_bfs(self):
        # Test BFS on connected graph
        result = bfs(self.graph, 'A')
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.assertEqual(result, expected)

    def test_dfs_disconnected(self):
        # Test DFS on disconnected graph
        visited = set()
        result = []
        for node in self.disconnected_graph:
            if node not in visited:
                result.extend(dfs(self.disconnected_graph, node, visited))
        expected = ['A', 'B', 'C', 'D']
        self.assertEqual(result, expected)

    def test_bfs_disconnected(self):
        # Test BFS on disconnected graph
        visited = set()
        result = []
        for node in self.disconnected_graph:
            if node not in visited:
                result.extend(bfs(self.disconnected_graph, node))
        expected = ['A', 'B', 'C', 'D']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
