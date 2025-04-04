"""
Даденa е табла со димензии 6х6.
Во таблата се поставени М дрвја на случајни (меѓусебно различни) позиции кои се дадени на влез.
Ваша задача е да поставите M шатори во таблата.
Шаторите треба да се поставени на различни локации и не смеат да се поклопуваат со позициите на дрвјата.
Пример на сликата Tents.

Дополнително треба да важат следните ограничувања:
- На секое дрво мора да има сврзано точно еден шатор, хоризонтално или вертикално.
- Eден шатор може да биде соседен на повеќе дрвја и едно дрво да има повеќе од еден шатор соседно од него.
- На секое од дрвјата мора да е доделен точно еден од шаторите, и секој шатор може да е доделен на само едно дрво.
- Два шатори не смее да бидат поставени соседно еден до друг - ниту дијагонално!

За сите тест примери големината на таблата е 6х6. Бројот на дрвја/шатори и позициите на секое дрво се читаат од влез.

Ваша задача е да додадете променливи, да ги додадете домените на променливите,
како и да ги додадете ограничувањата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,
MinSumConstraint, InSetConstraint, NotInSetConstraint, SomeInSetConstraint, SomeNotInSetConstraint.

Input:
7
0 1
3 1
5 1
4 2
3 3
5 4
2 5

Result:
0 0
2 1
4 1
4 3
2 3
5 5
1 5
"""

from constraint import *


def not_adjacent(tree1, tree2):
    if max(abs(tree1[0] - tree2[0]), abs(tree1[1] - tree2[1])) < 2:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    n = int(input())
    trees = [tuple(map(int, input().split(" "))) for _ in range(n)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for tree in trees:
        domain = []
        for (x, y) in directions:
            if 0 <= tree[0] + x < 6 and 0 <= tree[1] + y < 6:
                domain.append((tree[0] + x, tree[1] + y))
        problem.addVariable(tree, domain)

    problem.addConstraint(AllDifferentConstraint(), trees)

    for tree1 in trees:
        for tree2 in trees:
            if tree1 != tree2:
                problem.addConstraint(not_adjacent, (tree1, tree2))

    solution = problem.getSolution()

    for tree in trees:
        tent = solution[tree]
        print(f"{tent[0]} {tent[1]}")
