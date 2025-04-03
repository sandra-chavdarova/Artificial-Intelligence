"""
Потребно е да направите распоред за презентација на трудови за некоја конференција.
На конференцијата треба да бидат презентирани вкупно 10 трудови од неколку области:
Вештачка интелигенција (AI), Машинско Учење (ML) и Обработка на природни јазици (NLP).

Ваша задача е да направите распоред за конференција по термини и при тоа да се земат предвид следните ограничувања:
- Во секој од термините може да бидат презентирани најмногу 4 трудови.
- Ако бројот на трудови од дадена област е помал или еднаков на максималниот број трудови кои може да бидат презентирани во даден термин, тогаш тие трудови треба да бидат распределени во ист термин.

Од стандарден влез се чита бројот на термини во кои треба да бидат распределени трудовите
(Напомена: бројот на термини секогаш ќе биде 3 или 4).
Потоа се читаат информации за секој труд во следниот формат „ID област“.

На стандарден излез да се испечати терминот за презентација за секој труд.
Напомена: решението ќе се смета за точно доколку ги добиете истите групи на трудови распределени во различен термин.
На пример, следните 2 можни распределби се сметаат за идентични:
Paper1 (AI): T1, Paper2 (AI): T1, Paper3 (ML): T2
Paper1 (AI): T2, Paper2 (AI): T2, Paper3 (ML): T1

Даден е почетен код со кој е креирана класа за претставување на проблемот, на кој се додадени променливите.
Потоа се повикува наоѓање на решение со BacktrackingSolver.
Ваша задача е да ги додадете домените на променливите, како и да ги додадете ограничувањата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи:
AllDifferentConstraint, AllEqualConstraint, MaxSumConstraint, ExactSumConstraint, MinSumConstraint,
InSetConstraint, NotInSetConstraint, SomeInSetConstraint, SomeNotInSetConstraint.

Input:
3
Paper1 AI
Paper2 ML
Paper3 AI
Paper4 AI
Paper5 NLP
Paper6 ML
Paper7 ML
Paper8 NLP
Paper9 NLP
Paper10 ML
end

Result:
Paper1 (AI): T3
Paper2 (ML): T2
Paper3 (AI): T3
Paper4 (AI): T3
Paper5 (NLP): T1
Paper6 (ML): T2
Paper7 (ML): T2
Paper8 (NLP): T1
Paper9 (NLP): T1
Paper10 (ML): T2
"""

from constraint import *


def papers_per_timeslot(*papers):
    timeslots = set(papers)
    for t in timeslots:
        if papers.count(t) > 4:
            return False
    return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    variables = [k for k in papers.keys()]
    papers_AI = [k for k, v in papers.items() if v == "AI"]
    papers_ML = [k for k, v in papers.items() if v == "ML"]
    papers_NLP = [k for k, v in papers.items() if v == "NLP"]

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    problem.addVariables(variables, domain)

    problem.addConstraint(papers_per_timeslot, variables)

    if 0 < len(papers_AI) <= 4:
        problem.addConstraint(AllEqualConstraint(), papers_AI)
    if 0 < len(papers_ML) <= 4:
        problem.addConstraint(AllEqualConstraint(), papers_ML)
    if 0 < len(papers_NLP) <= 4:
        problem.addConstraint(AllEqualConstraint(), papers_NLP)

    result = problem.getSolution()

    for paper in variables:
        topic = papers[paper]
        time = result[paper]
        print(f"{paper} ({topic}): {time}")
