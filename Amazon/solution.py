def criticalConnections(n, connections):
    # 1. Build the Adjacency List
    adj = [[] for _ in range(n)]
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    
    ranks = [-1] * n
    results = []
    
    def dfs(node, depth, parent):
        ranks[node] = depth
        min_back_rank = depth
        
        print(f"{'  ' * depth}→ Visiting Node {node} (Rank {depth})")
        
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            
            if ranks[neighbor] != -1:
                # Cycle found!
                print(f"{'  ' * depth}  [!] Cycle detected: Node {node} can reach back to Node {neighbor} (Rank {ranks[neighbor]})")
                min_back_rank = min(min_back_rank, ranks[neighbor])
            else:
                # Move deeper
                recursive_rank = dfs(neighbor, depth + 1, node)
                
                # Check Bridge Condition
                if recursive_rank > depth:
                    print(f"{'  ' * depth}  [*] BRIDGE FOUND: [{node}, {neighbor}] because {recursive_rank} > {depth}")
                    results.append([node, neighbor])
                else:
                    print(f"{'  ' * depth}  [ ] Edge [{node}, {neighbor}] is part of a cycle (can reach Rank {recursive_rank})")
                
                min_back_rank = min(min_back_rank, recursive_rank)
        
        print(f"{'  ' * depth}← Finished Node {node}, returning Min Rank {min_back_rank}")
        return min_back_rank

    print("--- Starting DFS Execution ---")
    dfs(0, 0, -1)
    return results

# Example 1
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

print(f"Network: {connections}")
final_bridges = criticalConnections(n, connections)
print("\nFinal Critical Connections:", final_bridges)