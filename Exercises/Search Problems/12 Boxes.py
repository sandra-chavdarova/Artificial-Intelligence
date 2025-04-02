"""
Дадена е табла NxN во кој се движи човече.
Во таблата има кутии кои се поставени на случајни позиции.
Човечето на почеток има даден број на топки m.
Потребно е човечето да ги внесе сите топки во кутиите, со тоа што во секоја кутија треба да има точно една топка.
Човечето може да постави топка во некоја кутија ако се наоѓа на некое поле соседно на полето на кое се наоѓа кутијата.
И дијагоналните полиња се сметаат за соседни. Човечето се движи во две насоки: горе и десно.
Човечето не смее да стапне на поле на кое се наоѓа кутија и не смее да излезе од границите на таблата.
Пример за почетна состојба е прикажан на сликата Boxes.

За сите тест примери големината на таблата n се чита од стандарден влез.
Потоа се чита бројот на кутии/топки и позициите на секоја кутија.
Почетната позиција на човечето секогаш е (0, 0).
Ваша задача е да го имплементирате движењето на човечето во successor функцијата.
Акциите се именуваат како „Gore/Desno“. Ако нема решение, потребно е да се испечати "No Solution!".
Потребно е проблемот да се реши во најмал број на чекори со примена на неинформирано пребарување.

Input:
5
4
1,1
2,2
3,3
4,4

Result:
['Gore', 'Gore', 'Gore', 'Desno', 'Gore', 'Desno', 'Desno']
"""

from searching_framework import *


class Boxes(Problem):
    def __init__(self, initial, boxes, n, goal=None):
        super().__init__(initial, goal)
        self.boxes = boxes
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == len(self.boxes)

    def successor(self, state):
        successors = dict()
        man = state[0]
        filled_boxes = state[1]
        remaining_balls = state[2]

        moves = {"Gore": (0, 1), "Desno": (1, 0)}

        for move, (x, y) in moves.items():
            if 0 <= man[0] + x < self.n and 0 <= man[1] + y < self.n and (man[0] + x, man[1] + y) not in self.boxes:
                new_filled_boxes = list(filled_boxes)
                new_remaining = remaining_balls
                new_x = man[0] + x
                new_y = man[1] + y
                for box in self.boxes:
                    if box not in new_filled_boxes and \
                            max(abs(box[0] - new_x), abs(box[1] - new_y)) == 1 and \
                            new_remaining > 0:
                        new_remaining -= 1
                        new_filled_boxes.append(box)
                successors[move] = ((new_x, new_y), tuple(new_filled_boxes), new_remaining)

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    initial_state = (man_pos, (), num_boxes)
    problem = Boxes(initial_state, boxes, n)
    result = breadth_first_graph_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
