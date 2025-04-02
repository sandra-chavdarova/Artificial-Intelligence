"""
Даден ни е 4x4 магичен квадрат.
Треба да ги пополниме ќелиите со различни природни броеви во ранг 1,2,…,16
така што секоја ќелија ќе содржи различен број и сумата на секој ред, колона и дијагонала ќе биде 34.
"""

from constraint import *
from django.db.models.expressions import result

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = range(16)
    domain = range(1, 17)
    problem.addVariables(variables, domain)
    sum = 34

    for first in [0, 4, 8, 12]:
        row = [first + move for move in range(4)]
        problem.addConstraint(ExactSumConstraint(sum), row)
    for first in [0, 1, 2, 3]:
        column = [first + move for move in range(0, 16, 4)]
        problem.addConstraint(ExactSumConstraint(sum), column)

    main_diagonal = [move for move in range(0, 16, 5)]
    minor_diagonal = [move for move in range(0, 12, 3)]
    problem.addConstraint(ExactSumConstraint(sum), main_diagonal)
    problem.addConstraint(ExactSumConstraint(sum), minor_diagonal)

    problem.addConstraint(AllDifferentConstraint(), variables)

    result = problem.getSolution()
    print(result)

    for i in range(16):
        if i % 4 == 0:
            print()
        print(str(result.get(i)) + "\t", end="")
