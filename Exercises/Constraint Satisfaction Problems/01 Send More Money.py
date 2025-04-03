"""
SEND+MORE=MONEY е криптоаритметичка загатка, што значи дека станува збор за наоѓање цифри
кои ги заменуваат буквите за да се направи математичкиот израз вистинит.
Секоја буква во проблемот претставува една цифра (0–9).
Две букви не можат да ја претставуваат истата цифра.
Кога буквата се повторува, тоа значи дека цифрата се повторува во решението.

    S E N D
+   M O R E
---------------
  M O N E Y

Даден е почетен код со кој е креирана класа за претставување на проблемот,
на кој се додадени променливите со нивниот домен.
Потоа се повикува наоѓање на решение со BacktrackingSolver.
Ваша задача е да го/ги додадете ограничувањето/њата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните
ограничувања како класи:  AllDifferentConstraint, AllEqualConstraint,
MaxSumConstraint, ExactSumConstraint,  MinSumConstraint, InSetConstraint,
NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.
"""

from constraint import *


def is_valid(s, e, n, d, m, o, r, y):
    # D + E = Y
    carry1 = (d + e) // 10
    if (d + e) % 10 != y:
        return False

    # N + R = E
    carry2 = (n + r + carry1) // 10
    if (n + r + carry1) % 10 != e:
        return False

    # E + O = N
    carry3 = (e + o + carry2) // 10
    if (e + o + carry2) % 10 != n:
        return False

    # S + M = O
    carry4 = (s + m + carry3) // 10
    if (s + m + carry3) % 10 != o:
        return False

    # M
    if carry4 != m:
        return False

    return True


if __name__ == '__main__':
    problem = Problem()
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    domain = range(10)
    problem.addVariables(variables, domain)

    problem.addConstraint(is_valid, variables)
    problem.addConstraint(AllDifferentConstraint(), variables)

    print(problem.getSolution())
