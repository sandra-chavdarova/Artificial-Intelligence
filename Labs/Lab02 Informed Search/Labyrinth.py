"""
Даден е лавиринт NxN во кој се движи човече.
Во лавиринтот има ѕидови кои се поставени на случајни позиции и истите не може да се прескокнуваат.
Потребно е човечето да стигне до куќичката без притоа да удри во некој ѕид или да излезе надвор од лавиринтот.
Човечето во четири насоки: горе, долу, лево и десно.
Со еден потег човечето во десно може да се помести за две или три позиции,
а во сите останати насоки може да се помести само за една позиција.
Пример за почетна состојба е прикажан на сликата Labyrinth:

За сите тест примери големината на таблата n се чита од стандарден влез.
Потоа се чита бројот на ѕидови и позициите на секој ѕид.
На крај се читаат позициите на човечето и куќичката.
Ваша задача е да го имплементирате движењето на човечето во successor функцијата.
Акциите се именуваат како „Desno X/Gore/Dolu/Levo“.
Потоа имплементирајте ја евристичката функција h.
Потребно е проблемот да се реши во најмал број на чекори со примена на информирано пребарување.

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
['Gore', 'Desno 2', 'Gore', 'Desno 2', 'Gore', 'Gore']
"""

from searching_framework import *


class Labyrinth(Problem):
    def __init__(self, initial, obstacles, n, goal):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.n = n

    def successor(self, state):
        successors = dict()
        man = state
        moves = {"Desno 2": (2, 0), "Desno 3": (3, 0), "Gore": (0, 1), "Dolu": (0, -1), "Levo": (-1, 0)}

        # move, offset (x, y)
        for move, (x, y) in moves.items():
            if 0 <= man[0] + x < self.n and 0 <= man[1] + y < n and (man[0] + x, man[1] + y) not in self.obstacles:
                if move == "Desno 2" and (man[0] + 1, man[1]) in self.obstacles:
                    continue
                elif move == "Desno 3" and \
                        ((man[0] + 1, man[1]) in self.obstacles or (man[0] + 2, man[1]) in self.obstacles):
                    continue
                else:
                    successors[move] = (man[0] + x, man[1] + y)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        state = node.state
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
    labyrinth = Labyrinth(man, tuple(obstacles), n, house)
    result = astar_search(labyrinth)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")
