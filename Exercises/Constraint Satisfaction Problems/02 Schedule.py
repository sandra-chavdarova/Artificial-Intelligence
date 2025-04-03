"""
Потребно е да се направи распоред на часови за една група студенти.
Студентите слушаат 4 предмети: Вештачка интелигенција (AI), Машинско учење (ML), Роботика (R) и Биоинформатика (BI).
За секој предмет треба да се закажат термини за предавања и вежби.
Бројот на термини за предавања за секој предмет се прима на влез.
Бројот на термини за вежби е секогаш 1 (ако за тој предмет има вежби).
Еден термин трае 2 часа. Почетокот на терминот може да биде на секој час,
односно терминот може да почне во 12:00, но не во 12:05, 12:10 итн.

За секој од предметите дадени се времињата во кои може да се одржат (дадено е времето на можен почеток на терминот):
- Вештачка интелигенција (предавања): понеделник, среда, петок во 11:00 и 12:00 часот
- Вештачка интелигенција (вежби): вторник и четврток во 10:00, 11:00, 12:00 и 13:00 часот
- Машинско учење (предавања): понеделник, среда, петок во 12:00, 13:00 и 15:00 часот
- Машинско учење (вежби): вторник и четврток во 11:00, 13:00 и 14:00 часот
- Роботика (предавања): понеделник, среда, петок во 10:00, 11:00, 12:00, 13:00, 14:00 и 15:00 часот
- Роботика (вежби): нема
- Биоинформатика (предавања): понеделник, среда, петок во 10:00 и 11:00 часот
- Биоинформатика (вежби): вторник и четврток во 10:00 и 11:00 часот

За термините важат следните ограничувања:
- Не смее да има преклопување на термините
- Предавањата и вежбите за Машинско учење мора да почнуваат во различно време
(пр. ако има час во понделник кој почнува во 12 часот, тогаш не смее да има термин по Машинско учење кој почнува во 12 другите денови)

Доколу има повеќе часови по некој предмет, не мора час 1 да доаѓа пред час 2.

Даден е почетен код со кој е креирана класа за претставување на проблемот и домените на променливите.
Потоа се повикува наоѓање на решение со BacktrackingSolver.
Ваша задача е да ги дефинирате променливите, како и да ги додадете ограничувањата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint,  MinSumConstraint,
InSetConstraint, NotInSetConstraint, SomeInSetConstraint,  SomeNotInSetConstraint.

Input:
1
1
1
1

Result:
{'ML_vezbi': 'Thu_14', 'ML_cas_1': 'Fri_15', 'BI_vezbi': 'Thu_11', 'AI_vezbi': 'Tue_13', 'AI_cas_1': 'Fri_12', 'BI_cas_1': 'Fri_10', 'R_cas_1': 'Wed_15'}
"""

from constraint import *


def not_equal_time(class1, class2):
    new_class1 = class1.split("_")
    new_class2 = class2.split("_")
    day1, day2 = new_class1[0], new_class2[0]
    hour1, hour2 = int(new_class1[1]), int(new_class2[1])
    if day1 == day2 and abs(hour1 - hour2) <= 1:
        return False
    return True


def ML_different_time(class1, class2):
    new_class1 = class1.split("_")
    new_class2 = class2.split("_")
    day1, day2 = new_class1[0], new_class2[0]
    hour1, hour2 = int(new_class1[1]), int(new_class2[1])
    if day1 == day2 and hour1 == hour2:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    AI_classes = []
    for i in range(casovi_AI):
        AI_classes.append(f"AI_cas_{i + 1}")

    ML_classes = []
    for i in range(casovi_ML):
        ML_classes.append(f"ML_cas_{i + 1}")

    R_classes = []
    for i in range(casovi_R):
        R_classes.append(f"R_cas_{i + 1}")

    BI_classes = []
    for i in range(casovi_BI):
        BI_classes.append(f"BI_cas_{i + 1}")

    problem.addVariables(AI_classes, AI_predavanja_domain)
    problem.addVariables(ML_classes, ML_predavanja_domain)
    problem.addVariables(R_classes, R_predavanja_domain)
    problem.addVariables(BI_classes, BI_predavanja_domain)

    AI_exercises = ["AI_vezbi"]
    ML_exercises = ["ML_vezbi"]
    BI_exercises = ["BI_vezbi"]
    problem.addVariables(AI_exercises, AI_vezbi_domain)
    problem.addVariables(ML_exercises, ML_vezbi_domain)
    problem.addVariables(BI_exercises, BI_vezbi_domain)

    all_classes = AI_classes + AI_exercises + ML_exercises + ML_classes + R_classes + BI_exercises + BI_classes

    for class1 in all_classes:
        for class2 in all_classes:
            if class1 != class2:
                problem.addConstraint(not_equal_time, (class1, class2))

    ML_all_classes = ML_classes + ML_exercises
    for class1 in ML_all_classes:
        for class2 in ML_all_classes:
            if class1 != class2:
                problem.addConstraint(ML_different_time, (class1, class2))

    solution = problem.getSolution()

    print(solution)
