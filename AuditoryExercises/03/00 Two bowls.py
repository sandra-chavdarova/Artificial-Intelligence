from searching_framework.uninformed_search import *


class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        successors = dict()
        j0, j1 = state
        c0, c1 = self.capacities

        if j0 > 0:
            successors["Empty J0"] = (0, j1)
        if j1 > 0:
            successors["Empty J1"] = (j0, 0)
        if j0 > 0 and j1 < c1:
            delta = min(c1 - j1, j0)
            successors["Pour from J0 to J1"] = (j0 - delta, j1 + delta)
        if j1 > 0 and j0 < c0:
            delta = min(c0 - j0, j1)
            successors["Pour from J1 to J0"] = (j0 + delta, j1 - delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    container = Container([15, 5], (5, 5), (10, 0))

    print("BFS")
    result = breadth_first_graph_search(container)
    print(result.solution())
    print(result.solve())

    print("DFS")
    result = depth_first_graph_search(container)
    print(result.solution())
    print(result.solve())
