from CloneGraph import Node, clone_graph
from WaterFlow import pacific_atlantic
from Mineffortpath import min_effort
from RedundantCOnnections import find_redundant
from GraphValidTree import valid_tree
from Provinces import find_circle_num
from NetworkDelayTIme import network_delay
from Connect import min_cost_connect
from RottingOranges import oranges_rotting
from WordLadder import ladder_length
from FlightwithinK import cheapest_flight
from CourseSchedule1and2 import find_order, can_finish
from NoofIslands import num_islands

if __name__ == "__main__":
    assert num_islands([list("11000"), list("11000"), list("00100"), list("00011")]) == 3
    a, b, c = Node(1), Node(2), Node(3); a.neighbors = [b, c]; b.neighbors = [a]; c.neighbors = [a]
    ca = clone_graph(a); assert ca is not a and [x.val for x in ca.neighbors] == [2, 3] and ca.neighbors[0].neighbors[0] is ca
    assert can_finish(2, [[1,0]]) and not can_finish(2, [[1,0],[0,1]])
    o = find_order(4, [[1,0],[2,0],[3,1],[3,2]]); assert o[0] == 0 and o[-1] == 3 and len(o) == 4
    assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4 and oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1 and oranges_rotting([[0,2]]) == 0
    assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5 and ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert network_delay([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2 and network_delay([[1,2,1]], 2, 2) == -1
    assert min_cost_connect([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
    assert find_circle_num([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]) and not valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) and not valid_tree(4, [[0,1],[2,3]])
    assert find_redundant([[1,2],[1,3],[2,3]]) == [2,3]
    F = [[0,1,100],[1,2,100],[0,2,500]]
    assert cheapest_flight(3, F, 0, 2, 1) == 200 and cheapest_flight(3, F, 0, 2, 0) == 500
    assert min_effort([[1,2,2],[3,8,2],[5,3,5]]) == 2 and min_effort([[1,2,3],[3,8,4],[5,3,5]]) == 1
    pa = pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    assert pa == sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
    # random cross-check: Dijkstra vs Bellman-Ford style, DSU components vs BFS
    import random
    for _ in range(300):
        n = random.randint(2, 7); E = [[random.randrange(n), random.randrange(n), random.randint(1, 9)] for _ in range(random.randint(0, 12))]
        d = {}; 
        bf = [float('inf')]*n; bf[0] = 0
        for _ in range(n):
            for u, v, w in E:
                if bf[u]+w < bf[v]: bf[v] = bf[u]+w
        reach = sum(x < float('inf') for x in bf)
        r = network_delay(E, n, 1) if False else None
        E1 = [[u+1, v+1, w] for u, v, w in E]
        res = network_delay(E1, n, 1)
        assert res == (max(bf) if reach == n else -1)
    print("All 13 solutions pass.")