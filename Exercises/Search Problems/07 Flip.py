"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python
за да се реши следниот проблем за кој една можна почетна состојба е прикажана на Слика Flip1.

Tабла со димензии N x N се состои од бели и црни полиња.
Со избор (кликнување) на едно поле се прави промена на бојата на тоа поле и на сите негови непосредни соседи
(горе, долу, лево и десно) во спротивната боја, како што е прикажано на Слика Flip2.
Целта е сите полиња на таблата да бидат обоени во црна боја.
Потребно е проблемот да се реши во најмал број на потези т.е. со избирање (кликнување) на најмал можен број на полиња.

За сите тест примери обликот на таблата е ист како на примерот даден на Слика Flip1.
За секој тест пример се менува големината N на таблата, како и распоредот на црни и бели полиња на неа, соодветно.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.
Во променливата n ја имате големината на таблата (бројот на редици односно колони);
во променливата fields ја имате бојата на сите полиња на таблата
(по редослед: одлево - надесно, редица по редица, ако таблата ја гледате како матрица),
каде 1 означува дека полето е обоено во црна, а 0 означува дека полето е обоено во бела боја.

Изборот на полиња (потезите) потребно е да ги именувате на следниот начин:
x: redica, y: kolona
каде redica и kolona се редицата и колоната на избраното (кликнатото) поле (ако таблата ја гледате како матрица).

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите
секвенцата на потези која треба да се направи за да може сите полиња на таблата да бидат обоени во црна боја.
Треба да примените неинформирано пребарување.
Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.

Input:
3
0,0,0,1,0,0,1,1,0

Result:
['x: 0, y: 0', 'x: 0, y: 2', 'x: 1, y: 1', 'x: 2, y: 2']
"""

from searching_framework import *


class Flip(Problem):
    def __init__(self, initial, n, goal):
        super().__init__(initial, goal)
        self.n = n

    def successor(self, state):
        successors = dict()
        for x in range(self.n):
            for y in range(self.n):
                new_state = [list(row) for row in state]

                if 0 <= x < self.n and 0 <= y < self.n:
                    new_state[x][y] = 1 - new_state[x][y]
                if x - 1 >= 0:
                    new_state[x - 1][y] = 1 - new_state[x - 1][y]
                if x + 1 < self.n:
                    new_state[x + 1][y] = 1 - new_state[x + 1][y]
                if y - 1 >= 0:
                    new_state[x][y - 1] = 1 - new_state[x][y - 1]
                if y + 1 < self.n:
                    new_state[x][y + 1] = 1 - new_state[x][y + 1]

                new_state = tuple(tuple(row) for row in new_state)
                successors[f"x: {x}, y: {y}"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        for s, g in zip(state, self.goal):
            for x, y in zip(s, g):
                if x != y:
                    return False
        return True


if __name__ == "__main__":
    n = int(input())
    matrix = []
    goal_test = []
    fields = input().split(",")
    i = 0
    for _ in range(n):
        row = []
        g = []
        for _ in range(n):
            row.append(int(fields[i]))
            g.append(1)
            i += 1
        matrix.append(tuple(row))
        goal_test.append(tuple(g))
    # print(matrix)
    # print(goal_test)

    problem = Flip(tuple(matrix), n, tuple(goal_test))
    result = breadth_first_graph_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")
