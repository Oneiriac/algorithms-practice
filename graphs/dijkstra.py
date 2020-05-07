import math
import heapq
from typing import List, Dict, Tuple
from test_cases import weighted_undirected_adj_list


def dijkstra(adj_list: Dict[str, List[Tuple[str, int]]], source: str) -> Dict[str, int]:
    """
    Dijkstra's algorithm for adjacency lists.
    Time complexity: O(E*log V + V*log V) = O(E log V) for connected graphs
    Aux. space: O(V)
    """
    # Initialise source cost to zero, all other costs to infinity
    costs = {node: math.inf for node in adj_list.keys()}
    prev = {}
    costs[source] = 0
    prev[source] = None
    candidate_heap = []  # min-heap
    current_node = source
    while len(prev) < len(adj_list):  # O(V)
        candidate_nodes = adj_list[current_node]
        for c_node, edge_cost in candidate_nodes:  # O(E) across all loops
            # use cost as first tuple element for comparison
            c_cost = edge_cost + costs[current_node]
            if c_cost < costs[c_node]:  # ~O(1)
                costs[c_node] = c_cost
                heapq.heappush(candidate_heap, (c_cost, c_node))  # O(log V)
        # Get next node from min-heap
        _min_cost, next_node = heapq.heappop(candidate_heap)  # O(log V)
        prev[next_node] = current_node
        current_node = next_node
    return costs


if __name__ == "__main__":
    print(dijkstra(weighted_undirected_adj_list, "A"))
