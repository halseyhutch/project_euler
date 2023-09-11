# this is pretty easy to do by hand. but using directed graphs + topological 
# sorting is more robust if this happened to be a bigger problem.


from collections import defaultdict, deque


def create_graph(logins):

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for login in logins:
        for i in range(2):
            if login[i+1] not in graph[login[i]]:
                graph[login[i]].append(login[i+1])
                in_degree[login[i+1]] += 1

    return graph, in_degree


# see Kahn's algorithm
# https://en.wikipedia.org/wiki/Topological_sorting
# use a deque since we don't really care about midpoint access
def topological_sort(graph, in_degree):

    queue = deque([node for node in graph if in_degree[node] == 0])
    passcode = []

    while queue:
        node = queue.popleft()
        passcode.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(passcode)


def p79():
    with open('data/p79.txt', 'r') as file:
        logins = file.readlines()
    logins = [login.strip() for login in logins]
    graph, in_degree = create_graph(logins)
    passcode = topological_sort(graph, in_degree)
    return passcode


if __name__ == '__main__':
    print(p79())
