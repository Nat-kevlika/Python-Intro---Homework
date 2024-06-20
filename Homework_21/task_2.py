#graph has two directions : 1) A -> C -> E -> F and 2 ) A-> B -> D -> G
class Graph:
    pass

def add_edge(graph, start, end):
    if start not in graph:
        graph[start] = []
    graph[start].append(end)

def has_path(graph, start, end, checked=None):
    if checked is None:
        checked = set()
    checked.add(start)
    if start == end:
        return True
    if start not in graph:
        return False
    for linked_node in graph[start]:
        if linked_node not in checked:
            if has_path(graph, linked_node, end, checked):
                return True
    return False

def main():
    graph = {}


    edges = [
        ('A', 'B'), ('B', 'D'), ('D', 'G'),
        ('A', 'C'), ('C', 'E'), ('E', 'F')
    ]
    for edge in edges:
        add_edge(graph, edge[0], edge[1])


    start, end = input("Enter start and end points separated by a space (like this: A B): ").split()


    if has_path(graph, start, end):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
