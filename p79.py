<<<<<<< Updated upstream
# ASSUME: there are no duplicate digits in the (shortest) passcode
# ASSUME: thus, the final solution has eight digits
# this is pretty ugly. but it seemed like the closest match to my
# pen and paper solution.

def p79():
    
    with open('data/p79.txt') as f:
        logins = f.read().splitlines()
    candidates = [set('01236789') for x in range(8)]

    # work in sequentially from each side, using assumptions above.

    for l in logins:
        candidates[0].discard(l[1])
        candidates[0].discard(l[2])
        candidates[7].discard(l[0])
        candidates[7].discard(l[1])
    candidates[0], = candidates[0]
    candidates[7], = candidates[7]

    candidates[1].discard(candidates[0])
    candidates[6].discard(candidates[7])
    for l in logins:
        if l[0] != candidates[0]:
            candidates[1].discard(l[1])
        candidates[1].discard(l[2])
        if l[2] != candidates[7]:
            candidates[6].discard(l[1])
        candidates[6].discard(l[0])
    candidates[1], = candidates[1]
    candidates[6], = candidates[6]

    candidates[2] -= set(candidates[0:2])
    candidates[5] -= set(candidates[6:8])
    for l in logins:
        if l[0] not in candidates[0:2]:
            candidates[2].discard(l[1])
        if l[1] != candidates[1]:
            candidates[2].discard(l[2])
        if l[2] not in candidates[6:8]:
            candidates[5].discard(l[1])
        if l[1] != candidates[6]:
            candidates[5].discard(l[0])
    candidates[2], = candidates[2]
    candidates[5], = candidates[5]

    candidates[3] -= set(candidates[0:3])
    candidates[4] -= set(candidates[5:8])
    for l in logins:
        if l[0] not in candidates[0:3]:
            candidates[3].discard(l[1])
        if l[1] not in candidates[1:3]:
            candidates[3].discard(l[2])
        if l[2] not in candidates[5:8]:
            candidates[4].discard(l[1])
        if l[1] not in candidates[5:7]:
            candidates[4].discard(l[0])
    candidates[3], = candidates[3]
    candidates[4], = candidates[4]

    return "".join(candidates)

print(p79())
=======
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
>>>>>>> Stashed changes
