import sys, copy
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

def uc_step(graph: nx.Graph, )


def uc_search(graph, start: str, goal: str):
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
        'route': []
    }

    uc_step(graph, result, start, goal)

    return result


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
    result = uc_search(graph, start, goal)

    # print results
    # print(f'distance: {"infinity" if result["distance"] == float("inf") else result["distance"]}')
    # print('route:')
    # if result['route'] is None:
    #     print('none')
    # else:
    #     for link in result['route']:
    #         print(f'{link["from"]} to {link["to"]}, {link["distance"]} km')


if __name__ == '__main__':
    main()

