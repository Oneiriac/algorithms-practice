from queue import LifoQueue
from collections import OrderedDict
import test_cases


def depth_first_search(adj_list, source, target):
    parents = {}
    visited = OrderedDict()
    parents[source] = None

    # DFS uses a stack (LIFO) to pull from when a dead end occurs
    v_stack = LifoQueue()
    v_stack.put(source)

    while not v_stack.empty():
        v = v_stack.get()
        # Check if vertex is discovered after enqueueing/at dequeueing, unlike BFS
        if v not in visited:
            visited[v] = True
            for adj_v in adj_list[v]:
                v_stack.put(adj_v)
                if adj_v not in parents:
                    parents[adj_v] = v

    visited_order = list(visited.keys())

    # Reconstruct shortest path
    current = target
    path_to_target = [current]
    while current != source:
        path_to_target.append(parents[current])
        current = parents[current]
    path_to_target = list(reversed(path_to_target))

    return path_to_target, visited_order


if __name__ == "__main__":
    path_to_target, visited_order = depth_first_search(
        test_cases.unweighted_undirected_adj_list, "A", "G")
    print("Path to target:", " > ".join(path_to_target))
    print("Visited order:", " > ".join(visited_order))
