"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python
за да се реши следниот проблем за кој почетната состојба е прикажана на сликата.

Потребно е да се пренесат зелката, јарето, волкот и фармерот од источната страна на западната страна на реката.
Само фармерот го вози чамецот. Во чамецот има простор за двајца патници: фармерот и уште еден патник.

Ограничувања: Доколку останат сами (без присуство на фармерот):
- Јарето ја јаде зелката
- Волкот го јаде јарето

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print)
со кој ќе ја вратите секвенцата од позиции на актерите која одговара на секвенцата на движења
со која сите актери ќе бидат пренесени на западната страна на реката.

Треба да примените информирано пребарување. Дефинирајте соодветна хевристика која ќе биде прифатлива за проблемот.
"""
from searching_framework import *


def valid(state):
    farmer, wolf, lamb, cabbage = state
    if wolf == lamb and wolf != farmer:
        return False
    if lamb == cabbage and lamb != farmer:
        return False
    return True


class Farmer(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        # state = (farmer, wolf, lamb, cabbage) = (e, w, e, w)
        # e - east
        # w - west
        successors = dict()
        farmer, wolf, lamb, cabbage = state

        new_farmer = "w"
        if farmer == "w":
            new_farmer = "e"
        new_state = (new_farmer, wolf, lamb, cabbage)
        if valid(new_state):
            successors["Farmer_nosi_farmer"] = new_state

        if farmer == wolf:
            new_wolf = "w"
            if wolf == "w":
                new_wolf = "e"
            new_state = (new_farmer, new_wolf, lamb, cabbage)
            if valid(new_state):
                successors["Farmer_nosi_volk"] = new_state

        if farmer == lamb:
            new_lamb = "w"
            if lamb == "w":
                new_lamb = "e"
            new_state = (new_farmer, wolf, new_lamb, cabbage)
            if valid(new_state):
                successors["Farmer_nosi_jare"] = new_state

        if farmer == cabbage:
            new_cabbage = "w"
            if cabbage == "w":
                new_cabbage = "e"
            new_state = (new_farmer, wolf, lamb, new_cabbage)
            if valid(new_state):
                successors["Farmer_nosi_zelka"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        goal = self.goal
        value = 0
        for (x, y) in zip(state, goal):
            if x != y:
                value += 1
        return value


if __name__ == '__main__':
    initial_state = ('e', 'e', 'e', 'e')
    goal_state = ('w', 'w', 'w', 'w')

    farmer = Farmer(initial_state, goal_state)

    result = astar_search(farmer)
    print(result.solution())
