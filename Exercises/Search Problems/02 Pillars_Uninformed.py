"""
Во серија се наредени N кружни столбови со иста висина.
На почетокот, на само еден од столбовите наредени се M камени блокови во форма на крофни со различна големина.
Блоковите се наредени како кула т.н. најголемиот блок е поставен најдоле на столбот,
а секој блок после него е помал од својот претходник подолу.

Крајната цел е кулата од почетниот столб да се премести на некој друг столб,
т.ш. ќе биде запазен оригиналниот редослед на блоковите.

Ваша задача е преку техниката на неинформирано пребарување низ простор на состојби
да одредите кој е најмалиот број на чекори потребни да се пресметаат блоковите од почетниот столб до крајниот
т.ш. важи правилото дека во секој чекор само еден блок од врвот на некој столб може да се помести
на некој друг столб ако е помал од блокот на врвот на другиот столб или другиот столб е празен.
Во почетниот код дадено ви е читањето од стандарден влез на почетната и целната состојба на столбовите,
т.ш. секој столб е претставен со посебна торка а броевите ги означуваат големините на блоковите.
На стандарден излез испечатете го минималниот број на потребни чекори да се реши проблемот,
како и редоследот на потребните акции кои се во форматот MOVE TOP BLOCK FROM PILLAR i TO PILLAR j.

Input:
3,2,1;;
;;3,2,1

Result:
Number of action 7
['MOVE TOP BLOCK FROM PILLAR 1 TO PILLAR 3', 'MOVE TOP BLOCK FROM PILLAR 1 TO PILLAR 2', 'MOVE TOP BLOCK FROM PILLAR 3 TO PILLAR 2', 'MOVE TOP BLOCK FROM PILLAR 1 TO PILLAR 3', 'MOVE TOP BLOCK FROM PILLAR 2 TO PILLAR 1', 'MOVE TOP BLOCK FROM PILLAR 2 TO PILLAR 3', 'MOVE TOP BLOCK FROM PILLAR 1 TO PILLAR 3']
"""

from searching_framework import *


class Pillar(Problem):
    def __init__(self, initial, n, goal):
        super().__init__(initial, goal)
        self.n = n

    def successor(self, state):
        successors = dict()

        for i in range(self.n):
            if len(state[i]) != 0:
                top = state[i][-1]
                for j in range(self.n):
                    if i != j and (len(state[j]) == 0 or state[j][-1] >= top):
                        new_pillar_i = tuple(state[i][:-1])
                        new_pillar_j = list(state[j])
                        new_pillar_j.append(top)
                        new_pillar_j = tuple(new_pillar_j)

                        new_state = list(state)
                        new_state[i] = new_pillar_i
                        new_state[j] = new_pillar_j
                        new_state = tuple(new_state)
                        successors[f"MOVE TOP BLOCK FROM PILLAR {i + 1} TO PILLAR {j + 1}"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        for s, g in zip(state, self.goal):
            if s != g:
                return False
        return True


if __name__ == "__main__":
    info1 = input().split(";")
    info2 = input().split(";")
    initial_state = []
    goal_state = []
    for i in info1:
        if len(i) != 0:
            li = i.split(",")
            initial_state.append(tuple([int(k) for k in li]))
        else:
            initial_state.append(tuple(i))
    for i in info2:
        if len(i) != 0:
            li = i.split(",")
            goal_state.append(tuple([int(k) for k in li]))
        else:
            goal_state.append(tuple(i))
    initial_state = tuple(initial_state)
    goal_state = tuple(goal_state)
    # print(initial_state)
    # print(goal_state)
    pillar = Pillar(initial_state, len(initial_state), goal_state)
    result = breadth_first_graph_search(pillar)
    if result is not None:
        print("Number of action", result.path_cost)
        print(result.solution())
    else:
        print("No solution")
