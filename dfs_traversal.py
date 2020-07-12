def dfs_tree_traversal(n, edges, s):
    """Given a list of all edges of a graph with vertices 1 to n,
        will traverse the tree, depth first, without recursion.
        A stack is maintained, which describes the route taken to
        each node. The search starts at s."""

    edges_by_vertex = dict([(i, []) for i in range(n)])
    for edge in edges:
        edges_by_vertex[edge[0]].append(edge[1])
        edges_by_vertex[edge[1]].append(edge[0])

    discovered = {s}
    stack = [s]
    while stack:
        print(stack)
        v = stack[-1]
        undiscovered_daughters = [w for w in edges_by_vertex[v] if w not in discovered]
        if not undiscovered_daughters:
            stack.pop()
        else:
            stack.append(undiscovered_daughters[0])
            discovered.add(undiscovered_daughters[0])


dfs_tree_traversal(7, [[0, 1], [1, 2], [2, 3], [2, 5], [4, 5], [5, 6]], 0)
