import sys, copy, queue
import networkx as nx


# def uc_step(graph: nx.Graph, result, current, goal):
#     for to in graph.neighbors(current):
#         d = graph.get_edge_data(current, to)['distance']
#         new_res = copy.deepcopy(result)
#         new_res['distance'] += d
#         new_res['path'].append({'from': current, 'to': to, 'distance': d})
#
#         if to == goal:
#             return
#         uc_step(graph, result, to)

# def uc_step(graph: nx.Graph, result, start, goal, cost):
#     for


def uc_search(graph: nx.Graph, start: str, goal: str):
    """
    Uninformed search implementation for searching a graph
    :param graph:
    :param start: city name
    :param goal: city name
    :return:
    result = {
        'distance': 455,
        'route': [
            {'from': 'Bremen', 'to': 'Dortmund', 'distance': 234},
            {'from': 'Dortmund', 'to': 'Frankfurt', 'distance': 221},
        ],
    }
    """
    # TODO: infinite distance for loop
    result = {
        'route': [],
        'cost': float('inf'),
    }
    reached = {}
    frontier = queue.PriorityQueue()
    frontier.put((0, start))

    parent = frontier.get()
    while parent is not None and parent[0] < result['cost']:
        for child in graph.neighbors(parent[1]):
            cost = parent[0] + graph.get_edge_data(parent[1], child)['distance']
            if child not in reached.keys() or cost < reached[child]['cost']:
                reached[child] = {'cost': cost, 'route': None}
                frontier.put((cost, child))
                graph.nodes[child]['predecessor'] = parent[1]
                if child == goal and cost <= reached[child]['cost']:
                    result['cost'] = cost

        if frontier.empty():
            parent = None
        else:
            parent = frontier.get()

    backtrack_node = goal
    while graph.nodes[backtrack_node].get('predecessor'):
        pred = graph.nodes[backtrack_node].get('predecessor')
        print(pred)
        result['route'].append(pred)
        backtrack_node = pred

    return result['cost'], result['route']


def main():
    file = sys.argv[1]
    start = sys.argv[2]
    goal = sys.argv[3]

    # build graph:
    graph = nx.Graph()
    with open(file, 'r') as edges:
        line = edges.readline()[0:-1]
        while line != 'END OF INPUT':
            edge_fr, edge_to, edge_w = line.split(' ')
            graph.add_edge(edge_fr, edge_to, distance=float(edge_w))
            line = edges.readline()[0:-1]

    # call pathfinding function
    cost, route = uc_search(graph, start, goal)

    # print(result)
    print(f'distance: {"infinity" if cost == float("inf") else cost}')
    print('route:')
    if not route:
        print('none')
    else:
        print(route)


if __name__ == '__main__':
    main()

