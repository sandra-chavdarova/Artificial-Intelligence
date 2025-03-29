"""
Во табла со димензии 10x10 се наоѓаат змија и зелени јаболки.
Потребно е змијата да ги изеде зелените јаболки.
Змијата на почетокот зафаќа три полиња од таблата, едно поле за главата и две полиња за телото.
При секое јадење на зелена јаболка телото на змијата се издолжува на крајот за едно поле.
Во даден момент можни се три акции на движење на змијата: продолжи право, сврти лево и сврти десно.
При движењето на змијата треба да се внимава змијата да не се изеде сама себе
(колизија на главата на змијата со некој дел од телото) и да не излезе надвор од таблата.
Потребно е проблемот да се реши во најмал број на потези.

За сите тест примери изгледот и големината на таблата се исти.
За сите тест примери почетната позиција на змијата е иста.
За секој тест пример се менува бројот и почетната позиција на зелените јаболки.

Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.
Во променливата zeleni_jabolki се сочувани позициите на зелените јаболки.
Табелата се претставува како координатен систем со координати x и y почнувајќи од нула, па соодветно,
позициите се зададени како торка со прв елемент x и втор елемент y.

Движењата на змијата треба да ги именувате на следниот начин:
- ProdolzhiPravo - змијата се придвижува за едно поле нанапред
- SvrtiDesno - змијата се придвижува за едно поле на десно
- SvrtiLevo - змијата се придвижува за едно поле на лево

Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print)
со кој ќе ја вратите секвенцата на движења која змијата треба да ја направи за да може да ги изеде сите зелени јаболки.
Да се најде решението со најмал број на преземени акции употребувајќи информирано пребарување.
Дефинирајте прифатлива хевристичка функција за информираниот алгоритам.

Input:
2
6,9
2,7

Result:
['SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo']
"""

from searching_framework import *


def check(head, new_head, body, new_body, green):
    if 0 <= new_head[0] < 10 and 0 <= new_head[1] < 10 and new_head not in body:
        new_body.insert(0, head)
        head = new_head
        if new_head in green:
            green = tuple(g for g in green if g != new_head)
        else:
            new_body = new_body[:-1]
        return head, tuple(new_body), tuple(green), True
    else:
        return head, tuple(body), tuple(green), False


def forwad(head, body, green, direction):
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

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green)
    return new_head, new_body, new_green, direction


def right(head, body, green, direction):
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

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green)

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


def left(head, body, green, direction):
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

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green)

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
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        head = state[0]
        body = state[1]
        green = state[2]
        direction = state[3]

        new_head, new_body, new_green, new_direction = forwad(head, body, green, direction)
        if head != new_head and body != new_body:
            successors["ProdolzhiPravo"] = (new_head, new_body, new_green, new_direction)
        new_head, new_body, new_green, new_direction = right(head, body, green, direction)
        if head != new_head and body != new_body:
            successors["SvrtiDesno"] = (new_head, new_body, new_green, new_direction)
        new_head, new_body, new_green, new_direction = left(head, body, green, direction)
        if head != new_head and body != new_body:
            successors["SvrtiLevo"] = (new_head, new_body, new_green, new_direction)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0

    def h(self, node):
        head = node.state[0]
        green = node.state[2]
        if len(green) != 0:
            apple = green[0]
            minimum = abs(head[0] - apple[0]) + abs(head[1] - apple[1])
            for g in green:
                minimum = max(minimum, abs(head[0] - g[0]) + abs(head[1] - g[1]))
            return minimum
        else:
            return 0


if __name__ == "__main__":
    n = int(input())
    green_apples = [tuple(map(int, input().split(','))) for _ in range(n)]
    initial_state = ((0, 7), ((0, 8), (0, 9)), tuple(green_apples), "down")
    print(green_apples)
    snake = Snake(initial_state)
    result = astar_search(snake)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")
