"""
За дадено дрво кое се состои од N темиња и N − 1 ребра, да се нумерираат темињата со различни вредности
од 1 до N и ребрата со различни вредности од 1 до N − 1 за да важи следното:
За секое ребро K важи дека апсолутната разлика на темињата од кое е формирано реброто е исто K.

Влезот го задаваме на следнот начин - во првата линија се чита бројот на темиња n.
Темињата ќе ги означуваме како v1, v2,…, vn. Во следните n − 1 линии се читаат ребрата
во формат i,j што означува дека постои ребро меѓу темето vi и vj.

Input:
7
1,2
1,4
1,7
2,3
2,5
5,6
"""

from constraint import *


def edge_constraint(vertex1, vertex2, edge):
    return edge == abs(vertex2 - vertex1)


if __name__ == "__main__":
    n = int(input())
    edges = [input() for _ in range(n - 1)]
    vertices = [f"{i + 1}" for i in range(n)]

    problem = Problem(BacktrackingSolver())

    vertices_domain = [i + 1 for i in range(n)]
    edges_domain = [i + 1 for i in range(n - 1)]

    problem.addVariables(vertices, vertices_domain)
    problem.addVariables(edges, edges_domain)

    problem.addConstraint(AllDifferentConstraint(), vertices)
    problem.addConstraint(AllDifferentConstraint(), edges)

    for edge in edges:
        vertex1, vertex2 = edge.split(",")
        problem.addConstraint(edge_constraint, [vertex1, vertex2, edge])

    # print(problem.getSolution())
    result = problem.getSolutions()
    for solution in result:
        print(solution)
        print()
