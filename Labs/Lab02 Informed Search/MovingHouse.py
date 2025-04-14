"""
Дадена е табла 5x9, каде што е поставено човече.
Потребно е човечето со качување по ѕидот да стигне до врвот кој е означен со куќичка.

Човечето може да се движи во три насоки: горе, горе-десно и горе-лево за една или две позиции
(дијагонално, не е како фигурата коњ во шах). Човечето може и да остане на моменталното поле.
Притоа човечето може да се наоѓа само на полињата на кои е поставен зелен осумаголник.
Полињата кои не се означени со зелен осумаголник може да се прескокнуваат.
Човечето исто така не смее да излезе од таблата.
Куќичката е подвижна и се движи лево и десно за една позиција со секое поместување (или избор да не се помести) на човечето.
Таа може да застане на било кое поле во редот во кој се наоѓа.
Куќичката на почеток се движи во една насока, а кога ќе стигне до крајот на таблата ја менува насоката.
Единственото поле во најгорниот ред на кое може да застане човечето е она на кое се наоѓа куќичката.

На слика MovingHouse е покажана една можна почетна состојба на таблата.

За сите тест примери големината на таблата е иста, а позицијата на човечето и куќичката се менуваат и се читаат од стандарден влез.
Притоа куќичката секогаш се наоѓа во најгорниот ред.
Почетната насока на куќичката исто така се чита од стандарден влез.
Позицијата на дозволените полиња е иста за сите тест примери.
Ваша задача е да го имплементирате поместувањето на човечето и куќичката во successor функцијата.
Акциите се именуваат како „Stoj/Gore 1/Gore 2/Gore-desno 1/Gore-desno 2/Gore-levo 1/Gore-levo 2“.
Дополнително, потребно е да проверите дали сте стигнале до целта,
односно да ја имплементирате функцијата goal_test и да проверите дали состојбата е валидна.
Треба да примените информирано пребарување за да најдете решение со најмал број на чекори.

Input:
1,0
1,8
desno

Result:
['Gore 1', 'Gore 2', 'Gore-desno 2', 'Gore-levo 2', 'Gore-desno 1']
"""

import math

from searching_framework import *


def move_house(house, direction):
    new_house = house
    if direction == "desno":
        if house[0] + 1 == 4:
            direction = "levo"
        new_house = (house[0] + 1, house[1])
    elif direction == "levo":
        if house[0] - 1 == 0:
            direction = "desno"
        new_house = (house[0] - 1, house[1])
    return new_house, direction


class House(Problem):
    def __init__(self, initial, allowed, goal=None):
        super().__init__(initial, goal)
        self.allowed = allowed

    def successor(self, state):
        successors = dict()
        man_x, man_y = state[0]
        house = state[1]
        direction = state[2]

        moves = {"Stoj": (0, 0), "Gore 1": (0, 1), "Gore 2": (0, 2),
                 "Gore-desno 1": (1, 1), "Gore-desno 2": (2, 2),
                 "Gore-levo 1": (-1, 1), "Gore-levo 2": (-2, 2)}

        # move, offset (x, y)
        for move, (x, y) in moves.items():
            new_house, new_direction = move_house(house, direction)
            if 0 <= man_x + x < 5 and 0 <= man_y + y < 9 and (
                    (man_x + x, man_y + y) in allowed or (man_x + x, man_y + y) == new_house):
                successors[move] = ((man_x + x, man_y + y), new_house, new_direction)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    # def h(self, node):
    # man = node.state[0]
    # house = node.state[1]
    # manhattan
    # return (abs(man[0] - house[0]) + abs(man[1] - house[1])) / 5

    def h(self, node):
        man = node.state[0]
        house = node.state[1]
        # euclidean
        return int(math.sqrt((man[0] - house[0]) ** 2 + (man[1] - house[1]) ** 2)) // 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    man = input().split(",")
    man = int(man[0]), int(man[1])
    house = input().split(",")
    house = int(house[0]), int(house[1])
    direction = input()
    # print(man)
    # print(house)
    initial_state = man, house, direction
    problem = House(initial_state, tuple(allowed))
    result = astar_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")
