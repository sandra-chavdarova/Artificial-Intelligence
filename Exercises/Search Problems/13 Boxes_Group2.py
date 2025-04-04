"""
Дадена е табла NxN во кој се движи човече.
Во таблата има кутии кои се поставени на случајни позиции. Кутиите на почеток содржат по една топка.
Потребно е човечето да ги собере сите топки од кутиите.
Човечето може да собере топка од некоја кутија ако се наоѓа на некое поле соседно на полето на кое се наоѓа кутијата.
И дијагоналните полиња се сметаат за соседни.
Човечето се движи во две насоки: долу и лево.
Човечето не смее да стапне на поле на кое се наоѓа кутија и не смее да излезе од границите на таблата.
Пример за почетна состојба е прикажан на слика Boxes_Group2.

За сите тест примери големината на таблата n се чита од стандарден влез.
Потоа се чита бројот на кутии/топки и позициите на секоја кутија.
Почетната позиција на човечето секогаш е (n-1, n-1).
Ваша задача е да го имплементирате движењето на човечето во successor функцијата.
Акциите се именуваат како „Dolu/Levo“. Ако нема решение, потребно е да се испечати "No Solution!".
Потребно е проблемот да се реши во најмал број на чекори со примена на неинформирано пребарување.

Во почетниот код треба да стои man_pos = (n-1, n-1)

Input:
5
4
1,1
2,2
3,3
0,0

Result:
['Dolu', 'Dolu', 'Dolu', 'Levo', 'Dolu', 'Levo', 'Levo']
"""

from searching_framework import *


class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

    def successor(self, state):
        successors = dict()
        man = state[0]
        balls = state[1]

        moves = {"Dolu": (0, -1), "Levo": (-1, 0)}

        for move, (x, y) in moves.items():
            if 0 <= man[0] + x < self.n and 0 <= man[1] + y < self.n and (man[0] + x, man[1] + y) not in self.boxes:
                remaining = [ball for ball in balls if max(abs(man[0] + x - ball[0]), abs(man[1] + y - ball[1])) != 1]
                successors[move] = ((man[0] + x, man[1] + y), tuple(remaining))
        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (n - 1, n - 1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
    initial_state = (man_pos, tuple(boxes))
    problem = Boxes(initial_state, n, tuple(boxes))
    result = breadth_first_graph_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
