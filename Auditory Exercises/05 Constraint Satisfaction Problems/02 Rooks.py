"""
Дадена ни е 8x8 табла за шах.
Треба да се постават 8 топови на таблата така што ниеден топ да не се напаѓа.
Топовите може да се постават на било која позиција која сметаме дека е најсоодветна.
Единственото ограничување е дека не треба да се напаѓаат.
"""

from constraint import *

if __name__ == '__main__':
    problem = Problem(MinConflictsSolver())
    variables = ["canon_" + str(i) for i in range(8)]
    domain = range(8)

    problem.addVariables(variables, domain)
    problem.addConstraint(AllDifferentConstraint(), variables)

    result = problem.getSolution()
    print(result)

    for row in range(8):
        chosen_column = result["canon_" + str(row)]
        for column in range(8):
            print("R" if column == chosen_column else "_", end="")
        print()
