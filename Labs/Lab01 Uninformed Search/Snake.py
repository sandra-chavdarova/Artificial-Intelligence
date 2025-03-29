"""
„Во табла со димензии 10x10 се наоѓаат змија, зелени јаболки и црвени јаболки.
Потребно е змијата да ги изеде зелените јаболки, а да ги одбегнува црвените јаболки кои се отровни.
Змијата на почетокот зафаќа три полиња од таблата, едно поле за главата и две полиња за телото.
При секое јадење на зелена јаболка телото на змијата се издолжува на крајот за едно поле (пример Слика 2).
Во даден момент можни се три акции на движење на змијата: продолжи право, сврти лево и сврти десно.
При движењето на змијата треба да се внимава змијата да не се изеде сама себе
(колизија на главата на змијата со некој дел од телото) и да не излезе надвор од таблата.
Потребно е проблемот да се реши во најмал број на потези.“

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликата.
За сите тест примери почетната позиција на змијата е иста.
За секој тест пример се менува бројот и почетната позиција на зелените и црвените јаболки.

Во првата линија од влезот е даден бројот на зелени јаболки N,
а во следните N редови се дадени координатите на зелените јаболки.
Потоа е даден бројот на црвени јаболки M и нивните координати во наредните M редови.
Табелата се претставува како координатен систем со координати x и y почнувајќи од нула,
па соодветно, позициите се зададени како торка со прв елемент x и втор елемент y.

Движењата на змијата треба да ги именувате на следниот начин:
- ProdolzhiPravo - змијата се придвижува за едно поле нанапред
- SvrtiDesno - змијата се придвижува за едно поле на десно
- SvrtiLevo - змијата се придвижува за едно поле на лево
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print)
со кој ќе ја вратите секвенцата на движења која змијата треба да ја направи за да може да ги изеде сите зелени јаболки.
Да се најде решението со најмал број на преземени акции употребувајќи некој алгоритам за неинформирано пребарување.
Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.

Input:
6
3,7
4,7
5,7
5,5
3,5
3,9
5
3,8
4,6
0,6
1,6
2,6

Result:
['SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo', 'SvrtiDesno', 'ProdolzhiPravo', 'SvrtiLevo']
"""

from searching_framework import *


def check(head, new_head, body, new_body, green, new_green, red):
    if 0 <= new_head[0] < 10 and 0 <= new_head[1] < 10 and new_head not in red and new_head not in body:
        head = new_head
        new_body.insert(0, head)
        if new_head in green:
            new_green = tuple(g for g in green if g != new_head)
        else:
            new_body = new_body[:-1]
        return head, tuple(new_body), new_green, True
    else:
        return head, tuple(body), tuple(green), False


def forward(head, body, green, red, direction):
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

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green, new_green, red)
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

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green, new_green, red)

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

    new_head, new_body, new_green, changed = check(head, new_head, body, new_body, green, new_green, red)

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
        green, head, body, direction = state
        new_head, new_body, new_green, new_direction = forward(head, body, green, self.red, direction)
        if new_head != head and new_body != body:
            successors["ProdolzhiPravo"] = (new_green, new_head, new_body, new_direction)

        new_head, new_body, new_green, new_direction = right(head, body, green, self.red, direction)
        if new_head != head and new_body != body:
            successors["SvrtiDesno"] = (new_green, new_head, new_body, new_direction)

        new_head, new_body, new_green, new_direction = left(head, body, green, self.red, direction)
        if new_head != head and new_body != body:
            successors["SvrtiLevo"] = (new_green, new_head, new_body, new_direction)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[0]) == 0


if __name__ == '__main__':
    n = int(input())
    green_apples = []
    for i in range(n):
        coordinates = input().split(",")
        green_apples.append((int(coordinates[0]), int(coordinates[1])))
    m = int(input())
    red_apples = []
    for i in range(m):
        coordinates = input().split(",")
        red_apples.append((int(coordinates[0]), int(coordinates[1])))
    snake = ((0, 8), (0, 9))
    head = (0, 7)
    game = Snake((tuple(green_apples), head, snake, "down"), red_apples)
    result = breadth_first_graph_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("No solution")

