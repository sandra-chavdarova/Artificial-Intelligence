"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем
за кој една можна почетна состојба е прикажана на сликата на следниот слајд.

На табла 7x9 поставени се три атоми (внимавајте, двата H-атоми се различни: едниот има линк во десно, а другиот има линк во лево).
Полињата обоени во сива боја претставуваат препреки.

Играчот може да ја започне играта со избирање на кој било од трите атоми.
Играчот во секој момент произволно избира точно еден од трите атоми и го „турнува“ тој атом во една од четирите насоки:
горе, долу, лево или десно.

Движењето на „турнатиот“ атом продолжува во избраната насока се’ додека атомот не „удри“ во препрека
или во некој друг атом (атомот секогаш застанува на првото поле што е соседно на препрека или на друг атом во соодветната насока).

Не е возможно ротирање на атомите (линковите на атомите секогаш ќе бидат поставени како што се на почетокот на играта).
Исто така, не е дозволено атомите да излегуваат од таблата.

Целта на играта е атомите да се доведат во позиција во која ја формираат „молекулата“ прикажана десно од таблата.
Играта завршува во моментот кога трите атоми ќе бидат поставени во бараната позиција, во произволни три соседни полиња од таблата.

Потребно е проблемот да се реши во најмал број на потези.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликата.
За сите тест примери положбите на препреките се исти.
За секој тест пример се менуваат почетните позиции на сите три атоми, соодветно.
Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.

Движењата на атомите потребно е да ги именувате на следниот начин:

RightX - за придвижување на атомот X надесно (X може да биде H1, O или H2)
LeftX - за придвижување на атомот X налево (X може да биде H1, O или H2)
UpX - за придвижување на атомот X нагоре (X може да биде H1, O или H2)
DownX - за придвижување на атомот X надолу (X може да биде H1, O или H2)
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите
секвенцата на движења која треба да се направи за да може атомите од почетната позиција да се доведат до бараната позиција.

Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.
"""

from searching_framework import *


def right(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 < 8 and [x1 + 1, y1] not in obstacles and [x1 + 1, y1] != [x2, y2] and [x1 + 1, y1] != [x3, y3]:
        x1 += 1
    return x1


def left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1
    return x1


def up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1
    return y1


def down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1
    return y1


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        h1_x, h1_y = state[0], state[1]
        o_x, o_y = state[2], state[3]
        h2_x, h2_y = state[4], state[5]

        # H1
        x_new = right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors["RightH1"] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)

        x_new = left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors["LeftH1"] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)

        y_new = up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors["UpH1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        y_new = down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors["DownH1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        # O
        x_new = right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors["RightO"] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)

        x_new = left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors["LeftO"] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)

        y_new = up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors["UpO"] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)

        y_new = down(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors["DownO"] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)

        # H2
        x_new = right(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if x_new != h2_x:
            successors["RightH2"] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)

        x_new = left(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if x_new != h2_x:
            successors["LeftH2"] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)

        y_new = up(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if y_new != h2_y:
            successors["UpH2"] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)

        y_new = down(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if y_new != h2_y:
            successors["DownH2"] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # H1 - O - H2
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] == state[4] - 1


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]))

    result = breadth_first_graph_search(molecule)
    print(result.solution())
