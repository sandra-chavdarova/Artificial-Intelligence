"""
Дадена е сложувалка 3x3, на која има полиња со броеви од 1 до 8 и едно празно поле. Празното поле е обележано со ‘*’.
Проблемот е како да се стигне од некоја почетна распределба на полињата до некоја посакувана.

Акции: акциите ќе ги разгледуваме како придвижување на празното поле, па можни акции се:
- Горе
- Долу
- Лево
- Десно
При дефинирањето на акциите, мора да се внимава дали тие воопшто можат да се преземат во дадената сложувалка.

Состојбата ќе ја дефинираме како стринг кој ќе има 9 знаци (по еден за секое бројче, плус '*').
Притоа, стрингот ќе се пополнува со изминување на сложувалката од првиот кон третиот ред, од лево кон десно.
Пример: состојбата за почетната сложувалка е "*32415678", а за финалната сложувалка е "*12345678".

Хевристика
- Број на полиња кои не се на вистинското место
- Менхетен растојание до целната состојба

За да можеме да го дефинираме растојанието, потребно е да дефинираме координатен систем.
Почетокот на координатниот систем е поставен во долниот лев агол на сложувалката.
Дефинираме речник за координатите на секое поле од сложувалката.
Дефинираме функција која пресметува Менхетн растојание за сложувалката.
Оваа функција на влез прима два цели броеви, кои одговараат на две полиња на кои се наоѓаат броевите
за кои треба да пресметаме растојание.
"""

from searching_framework import *


class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        # "*32415678"
        #  0 1 2
        #  3 4 5
        #  6 7 8
        successors = dict()
        index = state.index("*")

        # up i-3
        if index > 2:
            temp = list(state)
            temp[index], temp[index - 3] = temp[index - 3], temp[index]
            new_state = "".join(temp)
            successors["Up"] = new_state

        # down i+3
        if index < 6:
            temp = list(state)
            temp[index], temp[index + 3] = temp[index + 3], temp[index]
            new_state = "".join(temp)
            successors["Down"] = new_state

        # right i+1
        if index % 3 != 2:
            temp = list(state)
            temp[index], temp[index + 1] = temp[index + 1], temp[index]
            new_state = "".join(temp)
            successors["Right"] = new_state

        # left i+1
        if index % 3 != 0:
            temp = list(state)
            temp[index], temp[index - 1] = temp[index - 1], temp[index]
            new_state = "".join(temp)
            successors["Left"] = new_state

        return successors

    def h(self, node):
        counter = 0
        for x, y in zip(node.state, self.goal):
            if x != y:
                counter += 1
        return counter

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


class Puzzle_h2(Puzzle):
    coordinates = {
        0: (0, 2), 1: (1, 2), 2: (2, 2),
        3: (0, 1), 4: (1, 1), 5: (2, 1),
        6: (0, 0), 7: (1, 0), 8: (2, 0)
    }

    @staticmethod
    def mhd(n, m):
        x1, y1 = Puzzle_h2.coordinates[n]
        x2, y2 = Puzzle_h2.coordinates[m]
        return abs(x2 - x1) + abs(y2 - y1)

    def h(self, node):
        sum_value = 0
        for i in "12345678":
            val = Puzzle_h2.mhd(node.state.index(i), int(i))
            sum_value += val
        return sum_value


if __name__ == '__main__':
    puzzle = Puzzle("*32415678", "*12345678")
    result1 = astar_search(puzzle)
    print(result1.solve())
    result2 = greedy_best_first_graph_search(puzzle)
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solution())

    puzzle2 = Puzzle_h2("*32415678", "*12345678")
    result4 = astar_search(puzzle2)
    print(result1.solve())
    result5 = greedy_best_first_graph_search(puzzle2)
    print(result2.solve())
    result6 = recursive_best_first_search(puzzle2)
    print(result3.solution())
