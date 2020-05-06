from queue import Queue
from collections import OrderedDict
import test_cases


def breadth_first_search(adj_list, source, target):
    parents = OrderedDict()  # To track order nodes were visited in
    v_queue = Queue()
    v_queue.put(source)

    while not v_queue.empty():
        current_v = v_queue.get()
        current_parent = parents.get(current_v)
        # if current_parent is None, vertex has not been visited
        for adj_v in adj_list[current_v]:
            # Prevent cycles by skipping parent of current_v
            # Check if vertex is visited *before* enqueuing, unlike DFS
            if adj_v != current_parent:
                v_queue.put(adj_v)
                parents[adj_v] = current_v

    visited_order = list(parents.keys())

    # Reconstruct shortest path
    current = target
    shortest_path = [current]
    while current != source:
        shortest_path.append(parents[current])
        current = parents[current]
    shortest_path = list(reversed(shortest_path))

    return shortest_path, visited_order


if __name__ == "__main__":
    shortest_path, visited_order = breadth_first_search(
        test_cases.unweighted_undirected_adj_list, "A", "G")
    print("Shortest path to target:", " > ".join(shortest_path))
    print("Visited order:", " > ".join(visited_order))
