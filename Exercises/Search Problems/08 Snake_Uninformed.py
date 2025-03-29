"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python
за да се реши следниот проблем за кој една можна почетна состојба е прикажана на Слика Snake1.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликата.
За сите тест примери почетната позиција на змијата е иста.
За секој тест пример се менува бројот и почетната позиција на зелените и црвените јаболки.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.
Во променливата crveni_jabolki се сочувани позициите на црвените јаболки (како листа од торки),
а во променливата zeleni_jabolki се сочувани позициите на зелените јаболки.
Табелата се претставува како координатен систем со координати x и y почнувајќи од нула, па соодветно,
позициите се зададени како торка со прв елемент x и втор елемент y.

Движењата на змијата треба да ги именувате на следниот начин:
- ProdolzhiPravo - змијата се придвижува за едно поле нанапред
- SvrtiDesno - змијата се придвижува за едно поле на десно
- SvrtiLevo - змијата се придвижува за едно поле на лево

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print)
со кој ќе ја вратите секвенцата на движења која змијата треба да ја направи за да може да ги изеде сите зелени јаболки.
Да се најде решението со најмал број на преземени акции употребувајќи некој алгоритам за неинформирано пребарување.
Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.

Input:
5
6,9
2,7
9,5
2,3
4,3
4
4,6
6,5
3,3
6,8

Result:
['SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo']
"""

from searching_framework import *


def check(head, new_head, body, new_body, green, red):
    if 0 <= new_head[0] < 10 and 0 <= new_head[1] < 10 and new_head not in red and new_head not in body:
        new_body.insert(0, head)
        head = new_head
        if new_head in green:
            green = tuple(g for g in green if g != new_head)
        else:
            new_body = new_body[:-1]
        return head, tuple(new_body), tuple(green), True
    else:
        return head, tuple(body), tuple(green), False


def forwad(head, body, green, red, direction):
    new_green = green
    new_body = list(body)
    new_head = head
    if direction == "down":
        new_head = (head[0], head[1] - 1)
    elif direction == "right":
        new_head = (head[0] + 1, head[1])
    elif direction == "up":
        new_head = (head[0], head[1] + 1)
    elif direction == "left":
        new_head = (head[0] - 1, head[1])

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green, red)
    return new_head, new_body, new_green, direction


def right(head, body, green, red, direction):
    new_green = green
    new_body = list(body)
    new_head = head
    if direction == "down":
        new_head = (head[0] - 1, head[1])
    elif direction == "right":
        new_head = (head[0], head[1] - 1)
    elif direction == "up":
        new_head = (head[0] + 1, head[1])
    elif direction == "left":
        new_head = (head[0], head[1] + 1)

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green, red)

    if changed:
        if direction == "down":
            direction = "left"
        elif direction == "right":
            direction = "down"
        elif direction == "up":
            direction = "right"
        elif direction == "left":
            direction = "up"
    return new_head, tuple(new_body), new_green, direction


def left(head, body, green, red, direction):
    new_green = green
    new_body = list(body)
    new_head = head
    if direction == "down":
        new_head = (head[0] + 1, head[1])
    elif direction == "right":
        new_head = (head[0], head[1] + 1)
    elif direction == "up":
        new_head = (head[0] - 1, head[1])
    elif direction == "left":
        new_head = (head[0], head[1] - 1)

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green, red)

    if changed:
        if direction == "down":
            direction = "right"
        elif direction == "right":
            direction = "up"
        elif direction == "up":
            direction = "left"
        elif direction == "left":
            direction = "down"
    return new_head, tuple(new_body), new_green, direction


class Snake(Problem):
    def __init__(self, initial, red, goal=None):
        super().__init__(initial, goal)
        self.red = red

    def successor(self, state):
        successors = dict()
        head = state[0]
        body = state[1]
        green = state[2]
        direction = state[3]

        new_head, new_body, new_green, new_direction = forwad(head, body, green, self.red, direction)
        if head != new_head and body != new_body:
            successors["ProdolzhiPravo"] = (new_head, new_body, new_green, new_direction)
        new_head, new_body, new_green, new_direction = right(head, body, green, self.red, direction)
        if head != new_head and body != new_body:
            successors["SvrtiDesno"] = (new_head, new_body, new_green, new_direction)
        new_head, new_body, new_green, new_direction = left(head, body, green, self.red, direction)
        if head != new_head and body != new_body:
            successors["SvrtiLevo"] = (new_head, new_body, new_green, new_direction)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    n = int(input())
    green_apples = []
    for _ in range(n):
        info = input().split(",")
        green_apples.append((int(info[0]), int(info[1])))
    m = int(input())
    red_apples = []
    for _ in range(m):
        info = input().split(",")
        red_apples.append((int(info[0]), int(info[1])))
    # print("Green", green_apples)
    # print("Red", red_apples)
    initial_state = ((0, 7), ((0, 8), (0, 9)), tuple(green_apples), "down")
    snake = Snake(initial_state, tuple(red_apples))
    result = breadth_first_graph_search(snake)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")
