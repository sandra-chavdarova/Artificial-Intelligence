"""
Во оваа верзија на задачата, човечето не смее да се движи во истата насока два пати по ред.
Ова значи дека не може да преземе ниту акции Desno 2, Desno 3 веднаш една после друга.
На почеток може да се движи во било која насока.

Input:
5
4
2,0
3,1
1,2
2,4
0,0
4,4

Result:
['Gore', 'Desno 2', 'Gore', 'Desno 2', 'Levo', 'Gore', 'Levo', 'Desno 2', 'Gore']
"""

from searching_framework import *


class Labyrinth(Problem):
    def __init__(self, initial, obstacles, n, goal):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.n = n

    def successor(self, state):
        successors = dict()
        man = state[0]
        direction = state[1]
        moves = {"Desno 2": (2, 0), "Desno 3": (3, 0), "Gore": (0, 1), "Dolu": (0, -1), "Levo": (-1, 0)}

        # move, offset (x, y)
        for move, (x, y) in moves.items():
            if 0 <= man[0] + x < self.n and 0 <= man[1] + y < self.n and (
                    man[0] + x, man[1] + y) not in self.obstacles and direction != move:
                if (move == "Desno 2" and (man[0] + 1, man[1]) in self.obstacles) \
                        or move == "Desno 2" and direction == "Desno 3":
                    continue

                elif (move == "Desno 3" and ((man[0] + 1, man[1]) in self.obstacles or (
                        man[0] + 2, man[1]) in self.obstacles)) or move == "Desno 3" and direction == "Desno 2":
                    continue

                else:
                    successors[move] = ((man[0] + x, man[1] + y), move)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal

    def h(self, node):
        state = node.state[0]
        goal = self.goal
        # manhattan
        return (abs(state[0] - goal[0]) + abs(state[1] - goal[1])) / 3


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    obstacles = []
    for _ in range(m):
        pair = input().split(",")
        pair = (int(pair[0]), int(pair[1]))
        obstacles.append(pair)
    man = input().split(",")
    man = (int(man[0]), int(man[1]))
    house = input().split(",")
    house = (int(house[0]), int(house[1]))
    # print(man)
    # print(house)
    # print(obstacles)
    initial_state = (man, "")
    labyrinth = Labyrinth(initial_state, tuple(obstacles), n, house)
    result = astar_search(labyrinth)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
