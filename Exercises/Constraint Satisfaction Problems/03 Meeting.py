"""
Потребно е да се закаже состанок во петок за Марија, Петар и Симона.
Симона како менаџер мора да присуствува на состанокот со најмалку уште една личност.
Состанокот трае еден час, и може да се закаже во периодот од 12:00 до 20:00.
Почетокот на состанокот може да биде на секој час, односно состанокот може да почне во 12:00, но не во 12:05, 12:10 итн.
За секој од членовите дадени се времињата во кои се слободни:

Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
Марија слободни термини: 14:00-16:00, 18:00-19:00
Петар слободни термини: 12:00-14:00, 16:00-20:00

Потребно е менаџерот Симона да ги добие сите можни почетни времиња за состанокот.
Даден е почетен код со кој е креирана класа за претставување на проблемот, на кој се додадени променливите.
Потоа се повикува наоѓање на решение со BacktrackingSolver.
Ваша задача е да ги додадете домените на променливите, како и да ги додадете ограничувањата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,  MinSumConstraint,
InSetConstraint, NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.

Result:
{'Simona_prisustvo': 1, 'Marija_prisustvo': 1, 'Petar_prisustvo': 0, 'vreme_sostanok': 14}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 19}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 16}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 13}
"""

from constraint import *


def manager(simona, time):
    if time not in range(13, 15) and time not in range(16, 17) and time not in range(19, 20):
        return False
    return True


def employee(marija, petar, time):
    if marija == 1 and time not in range(14, 16) and time not in range(18, 19):
        return False
    if petar == 1 and time not in range(12, 14) and time not in range(16, 20):
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    time = list(range(12, 21))
    domain = [0, 1]

    problem.addVariable("Marija_prisustvo", domain)
    problem.addVariable("Simona_prisustvo", domain)
    problem.addVariable("Petar_prisustvo", domain)
    problem.addVariable("vreme_sostanok", time)

    problem.addConstraint(MinSumConstraint(1), ["Simona_prisustvo"])
    problem.addConstraint(MinSumConstraint(2), ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"))
    problem.addConstraint(manager, ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(employee, ("Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))

    [print(solution) for solution in problem.getSolutions()]
