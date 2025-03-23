"""
Даден е лавиринт NxN во кој се движи Дух на ролери.
Во лавиринтот има ѕидови кои се поставени на случајни позиции и истите може да се прескокнуваат.
Потребно е Духот да стигне до Пакман без притоа да удри во некој ѕид или да излезе надвор од лавиринтот.
Духот се движи со помош на ролери во две насоки: горе и десно.
Со еден потег Духот може да се помести за една, две или три позиции горе или десно.
Пример за почетна состојба е прикажан на сликата GhostOnSkates.

За сите тест примери големината на таблата n се чита од стандарден влез.
Потоа се чита бројот на ѕидови и позициите на секој ѕид.
Почетната позиција на Духот секогаш е (0, 0), додека позицијата на Пакман секогаш е (n-1, n-1).
Ваша задача е да го имплементирате движењето на Духот во successor функцијата,
така што најпрво ќе се проба акцијата за движење горе, а потоа десно.
Акциите се именуваат како „Gore/desno X“.
Потоа имплементирајте ја хевристичката функција h.
Состојбата на проблемот се чува во торка каде што елементите се x и y позициите на Духот.
На пример, почетната состојба за дадената слика би била (0, 0).
Потребно е проблемот да се реши во најмал број на чекори со примена на информирано пребарување.

Input:
4
3
1,1
2,2
3,0

Result:
['Gore 3', 'Desno 3']
"""

from searching_framework import *


class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n

    def successor(self, state):
        successors = dict()
        ghost_x, ghost_y = state

        if self.check_valid((ghost_x, ghost_y + 1), self.walls, self.n):
            successors["Gore 1"] = (ghost_x, ghost_y + 1)
        if self.check_valid((ghost_x, ghost_y + 2), self.walls, self.n):
            successors["Gore 2"] = (ghost_x, ghost_y + 2)
        if self.check_valid((ghost_x, ghost_y + 3), self.walls, self.n):
            successors["Gore 3"] = (ghost_x, ghost_y + 3)

        if self.check_valid((ghost_x + 1, ghost_y), self.walls, self.n):
            successors["Desno 1"] = (ghost_x + 1, ghost_y)
        if self.check_valid((ghost_x + 2, ghost_y), self.walls, self.n):
            successors["Desno 2"] = (ghost_x + 2, ghost_y)
        if self.check_valid((ghost_x + 3, ghost_y), self.walls, self.n):
            successors["Desno 3"] = (ghost_x + 3, ghost_y)
        return successors

    @staticmethod
    def check_valid(state, walls, n):
        x, y = state
        if x < n and y < n and (x, y) not in walls:
            return True
        return False

    def h(self, node):
        x, y = node.state
        return (abs(x - self.goal[0]) + abs(y - self.goal[1])) / 3

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)
    result = astar_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")

