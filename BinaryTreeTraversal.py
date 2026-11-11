class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:

  def __init__(self):
    self.root = None

  def bfs(self):
    """Breadth-First Search (Level Order)"""
    if not self.root:
      return []
    result, queue = [], [self.root]
    while queue:
      curr = queue.pop(0)
      result.append(curr.value)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    return result

  def dfs(self, node, result=None):
    """Depth-First Search (Pre-order traversal)"""
    if result is None:
      result = []
    if node:
      result.append(node.value)
      self.dfs(node.left, result)
      self.dfs(node.right, result)
    return result


# Constructing the Binary Tree Diagram for VILLARINO
bt = BinaryTree()
bt.root = TreeNode("V")  # Level 0
bt.root.left = TreeNode("I")  # Level 1
bt.root.right = TreeNode("L")  # Level 1

bt.root.left.left = TreeNode("L")  # Level 2
bt.root.left.right = TreeNode("A")  # Level 2
bt.root.right.left = TreeNode("R")  # Level 2
bt.root.right.right = TreeNode("I")  # Level 2

bt.root.left.left.left = TreeNode("N")  # Level 3
bt.root.left.left.right = TreeNode("O")  # Level 3

if __name__ == "__main__":
  print("=== 1. BINARY TREE PROGRAM ===")
  print("BFS Traversal:", " -> ".join(bt.bfs()))
  print("DFS Traversal:", " -> ".join(bt.dfs(bt.root)))