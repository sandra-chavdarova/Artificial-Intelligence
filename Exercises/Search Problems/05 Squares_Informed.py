"""
Дадена е табла 5x5, каде што се поставени 5 сиви квадратчиња.
На почетокот 5те квадратчиња се поставени на случајни позиции во таблата.
Секое од квадратчињата има реден број, кој што одредува на кое поле по левата дијагонала на таблата
е потребно да се намести даденото квадратче. Пример на почетна состојба на таблата е даден на слика Squares1,
додека слика Squares2 ја прикажува состојбата на таблата која е целна.
Секое од квадратчињата може да се помести во четири насоки: горе, долу, лево и десно за една позиција.
Со еден потег може да се помести само едно црно квадратче, и притоа квадратчето не смее да се помести надвор од таблата,
а на едно исто поле може да се најдат повеќе квадратчиња.

За сите тест примери големината на таблата е иста, а позицијата на секоја од квадратчињата се чита од стандарден влез.
Ваша задача е да ја имплементирате хевристичката функција h во класата Squares.
Сите останати функции (sucessor, goal_test, actions, result) претпоставете дека се имплементирани во позадина.
Освен хевристичката функција, не имплементирајте ништо друго!!!
Состојбата на проблемот се чува во торка каде што елементите се x и y позициите на секое од квадратчињата,
претставени редоследно според бројот кој го претставуваат
(на прва позиција е квадратчето со број 1, на втора позција е квадратчето со број 2, итн.).
На пример, почетната состојба на слика 1 би била ((2, 4), (3, 1), (4, 1), (1, 2), (0, 0)).

Input:
2,4
1,3
2,2
3,1
4,0

Result:
['Pomesti kvadratche 1 levo', 'Pomesti kvadratche 1 levo']
"""

from searching_framework import *


class Squares(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        for (square, i) in zip(state, range(5)):
            square_x, square_y = square[0], square[1]
            if self.check_valid(square_x, square_y + 1):
                new_state = tuple()
                for j in range(5):
                    if i != j:
                        new_state += (state[j],)
                    else:
                        new_state += ((square_x, square_y + 1),)
                successors[f"Pomesti kvadratche {i + 1} gore"] = new_state
            if self.check_valid(square_x, square_y - 1):
                new_state = tuple()
                for j in range(5):
                    if i != j:
                        new_state += (state[j],)
                    else:
                        new_state += ((square_x, square_y - 1),)
                successors[f"Pomesti kvadratche {i + 1} dolu"] = new_state
            if self.check_valid(square_x + 1, square_y):
                new_state = tuple()
                for j in range(5):
                    if i != j:
                        new_state += (state[j],)
                    else:
                        new_state += ((square_x + 1, square_y),)
                successors[f"Pomesti kvadratche {i + 1} desno"] = new_state
            if self.check_valid(square_x - 1, square_y):
                new_state = tuple()
                for j in range(5):
                    if i != j:
                        new_state += (state[j],)
                    else:
                        new_state += ((square_x - 1, square_y),)
                successors[f"Pomesti kvadratche {i + 1} levo"] = new_state

        return successors

    def h(self, node):
        state = node.state
        goal = self.goal
        manhattans = 0
        for (s, g) in zip(state, goal):
            manhattans += abs(s[0] - g[0]) + abs(s[1] - g[1])
        return manhattans

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(x, y):
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))),)
    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))
    squares = Squares(initial_state, goal_state)
    result = astar_search(squares)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")
