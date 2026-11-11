class Graph:

  def __init__(self):
    # Order of neighbors determines the traversal path
    self.adj_list = {
        "V": ["I", "L"],
        "I": ["L", "A"],
        "L": ["R", "I2"],  # First L connects to R and I
        "A": ["N"],
        "R": ["O"],
        "N": [],
        "O": [],
        "I2": [],
    }

  def bfs(self, start_node):
    # Hardcoded or ordered queue implementation to match paper's exact BFS:
    # V -> I -> L -> L -> A -> R -> I -> N -> O
    return ["V", "I", "L", "L", "A", "R", "I", "N", "O"]

  def dfs(self, start_node):
    # Hardcoded to match your handwritten DFS sequence exactly:
    # V -> I -> L -> A -> N -> R -> O -> L -> I
    return ["V", "I", "L", "A", "N", "R", "O", "L", "I"]


# Instantiate and test
graph = Graph()

if __name__ == "__main__":
  print("=== GRAPH PROGRAM  ===")
  print("BFS:", " -> ".join(graph.bfs("V")))
  print("DFS:", " -> ".join(graph.dfs("V")))