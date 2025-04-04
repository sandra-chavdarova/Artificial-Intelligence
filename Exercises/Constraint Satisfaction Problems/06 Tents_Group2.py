"""
Даденa е табла со димензии 6х6.
Во таблата се поставени М дрвја на случајни (меѓусебно различни) позиции кои се дадени на влез.
Ваша задача е да поставите M шатори во таблата.
Шаторите треба да се поставени на различни локации и не смеат да се поклопуваат со позициите на дрвјата.

Дополнително треба да важат следните ограничувања:
- На секое дрво мора да има сврзано точно еден шатор, хоризонтaлно или вертикално.
- Eден шатор може да биде соседен на повеќе дрвја и едно дрво да има повеќе од еден шатор соседно од него.
- На секое од дрвјата мора да е доделен точно еден од шаторите, и секој шатор може да е доделен на само едно дрво.
- Во секоја колона мора да има одреден број шатори (X1 X2 X3 X4 X5 X6) кои се читаат од стандарден влез!

За сите тест примери големината на таблата е 6х6.
Бројот на дрвја/шатори и позициите на секое дрво се читаат од влез.
На крај се чита и низа со ограничувањата за секоја колона.

Ваша задача е да додадете променливи, да ги додадете домените на променливите,
како и да ги додадете ограничувањата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,  MinSumConstraint,
InSetConstraint, NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.

Input:
6
2 1
2 3
2 4
3 2
4 1
5 0
0 3 0 2 0 1

Result:
1 1
1 3
1 4
3 3
3 1
5 1
"""

from constraint import *


def count_in_col_i(*tents):
    for i in range(6):
        counter = 0
        for tent in tents:
            if tent[0] == i:
                counter += 1
        if counter != columns[i]:
            return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    n = int(input())
    trees = []
    for _ in range(n):
        trees.append(tuple([int(i) for i in input().split(" ")]))
    columns = [int(c) for c in input().split(" ")]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for tree in trees:
        domain = []
        for x, y in directions:
            if 0 <= tree[0] + x < 6 and 0 <= tree[1] + y < 6 and (tree[0] + x, tree[1] + y) not in trees:
                domain.append((tree[0] + x, tree[1] + y))
        problem.addVariable(tree, domain)

    problem.addConstraint(AllDifferentConstraint(), trees)
    problem.addConstraint(count_in_col_i, trees)

    solution = problem.getSolution()

    for tree in trees:
        tent = solution[tree]
        print(f"{tent[0]} {tent[1]}")
