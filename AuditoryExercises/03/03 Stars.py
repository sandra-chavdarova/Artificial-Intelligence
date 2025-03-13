"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој
една можна почетна состојба е прикажана на сликата.

На шаховска табла 8x8 поставени се еден коњ, еден ловец и три ѕвезди.
Движењето на коњите на шаховската табла е во облик на буквата Г:
притоа, од дадена позиција можни се 8 позиции до кои даден коњ може да се придвижи, како што е прикажано на сликата
(1 = горе + горе + лево, 2 = горе + горе + десно, 3 = десно + десно + горе, 4 = десно + десно + долу,
5 = долу + + долу + десно, 6 = долу + долу + лево, 7 = лево + лево + долу, 8 = лево + лево + горе).

Движењето на ловците на таблата е по дијагонала. Ловецот прикажан на сликата
може да се придвижи на кое било од полињата означени со X.

Целта на играта е да се соберат сите три ѕвезди.
Една ѕвезда се собира доколку некоја од фигурите застане на истото поле каде што се наоѓа и ѕвездата.

Притоа, не е дозволено двете фигури да бидат позиционирани на истото поле и не е дозволено фигурите да излегуваат од таблата.
Фигурите меѓусебно не се напаѓаат. Движењето на фигурите е произволно, т.е. во кој било момент може да се придвижи која било од двете фигури.
Потребно е проблемот да се реши во најмал број на потези.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликата.
За секој тест пример положбите на ѕвездите се различни.
Исто така, за секој тест пример се менуваат и почетните позиции на коњот и ловецот, соодветно.
Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.

Движењата на коњот потребно е да ги именувате на следниот начин:

K1 - за придвижување од тип 1 (горе + лево)
K2 - за придвижување од тип 2 (горе + десно)
K3 - за придвижување од тип 3 (десно + горе)
K4 - за придвижување од тип 4 (десно + долу)
K5 - за придвижување од тип 5 (долу + десно)
K6 - за придвижување од тип 6 (долу + лево)
K7 - за придвижување од тип 7 (лево + долу)
K8 - за придвижување од тип 8 (лево + горе)
Движењата на ловецот потребно е да ги именувате на следниот начин:

B1 - за придвижување од тип 1 (движење за едно поле во насока горе-лево)
B2 - за придвижување од тип 2 (движење за едно поле во насока горе-десно)
B3 - за придвижување од тип 3 (движење за едно поле во насока долу-лево)
B4 - за придвижување од тип 4 (движење за едно поле во насока долу-десно)
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print)
со кој ќе ја вратите секвенцата на движења која треба да се направи за да може фигурите да ги соберат сите три ѕвезди.
Треба да примените неинформирано пребарување.
Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.
"""

from searching_framework import *


def k1(x, y, bishop_x, bishop_y):
    if 0 <= x - 1 < 8 and 0 <= y + 2 < 8 and [x - 1, y + 2] != (bishop_x, bishop_y):
        x -= 1
        y += 2
    return x, y


def k2(x, y, bishop_x, bishop_y):
    if 0 <= x + 1 < 8 and 0 <= y + 2 < 8 and [x + 1, y + 2] != (bishop_x, bishop_y):
        x += 1
        y += 2
    return x, y


def k3(x, y, bishop_x, bishop_y):
    if 0 <= x + 2 < 8 and 0 <= y + 1 < 8 and [x + 2, y + 1] != (bishop_x, bishop_y):
        x += 2
        y += 1
    return x, y


def k4(x, y, bishop_x, bishop_y):
    if 0 <= x + 2 < 8 and 0 <= y - 1 < 8 and [x + 2, y - 1] != (bishop_x, bishop_y):
        x += 2
        y -= 1
    return x, y


def k5(x, y, bishop_x, bishop_y):
    if 0 <= x + 1 < 8 and 0 <= y - 2 < 8 and [x + 1, y - 2] != (bishop_x, bishop_y):
        x += 1
        y -= 2
    return x, y


def k6(x, y, bishop_x, bishop_y):
    if 0 <= x - 1 < 8 and 0 <= y - 2 < 8 and [x - 1, y - 2] != (bishop_x, bishop_y):
        x -= 1
        y -= 2
    return x, y


def k7(x, y, bishop_x, bishop_y):
    if 0 <= x - 2 < 8 and 0 <= y - 1 < 8 and [x - 2, y - 1] != (bishop_x, bishop_y):
        x -= 2
        y -= 1
    return x, y


def k8(x, y, bishop_x, bishop_y):
    if 0 <= x - 2 < 8 and 0 <= y + 1 < 8 and [x - 2, y + 1] != (bishop_x, bishop_y):
        x -= 2
        y += 1
    return x, y


def b1(x, y, knight_x, knight_y):
    if 0 <= x - 1 < 8 and 0 <= y + 1 < 8 and [x - 1, y + 1] != [knight_x, knight_y]:
        x -= 1
        y += 1
    return x, y


def b2(x, y, knight_x, knight_y):
    if 0 <= x + 1 < 8 and 0 <= y + 1 < 8 and [x + 1, y + 1] != [knight_x, knight_y]:
        x += 1
        y += 1
    return x, y


def b3(x, y, knight_x, knight_y):
    if 0 <= x - 1 < 8 and 0 <= y - 1 < 8 and [x - 1, y - 1] != [knight_x, knight_y]:
        x -= 1
        y -= 1
    return x, y


def b4(x, y, knight_x, knight_y):
    if 0 <= x + 1 < 8 and 0 <= y - 1 < 8 and [x + 1, y - 1] != [knight_x, knight_y]:
        x += 1
        y -= 1
    return x, y


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        knight_x = state[0]
        knight_y = state[1]

        bishop_x = state[2]
        bishop_y = state[3]

        stars = state[4]

        new_x, new_y = k1(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K1"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K2"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k3(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K3"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k4(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K4"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k5(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K5"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k6(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K6"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k7(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K7"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = k8(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["K8"] = (new_x, new_y, bishop_x, bishop_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = b1(bishop_x, bishop_y, knight_x, knight_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["B1"] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = b2(bishop_x, bishop_y, knight_x, knight_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["B2"] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = b3(bishop_x, bishop_y, knight_x, knight_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["B3"] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))
        new_x, new_y = b4(bishop_x, bishop_y, knight_x, knight_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors["B4"] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars if s[0] != new_x or s[1] != new_y]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == '__main__':
    knight = [2, 5]
    bishop = [5, 1]
    stars_pos = ((1, 1), (4, 3), (6, 6))

    stars = Stars((knight[0], knight[1], bishop[0], bishop[1], stars_pos))

    result = breadth_first_graph_search(stars)
    print(result.solution())
