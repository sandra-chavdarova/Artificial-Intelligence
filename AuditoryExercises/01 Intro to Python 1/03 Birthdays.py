"""
Во оваа задача се чуваат родендените на пријатели, кои треба да се пронајдат според имињата на пријателите.
Креирајте речник (dictionary) со имиња и родендени.
Потоа, додадете функционалност со која од стандарден влез се чита име на пријател,
и вратете го неговиот роденден (односно испечатете го на стандарден излез).
Интеракцијата на програмата треба да изгледа како:

Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:
Ana
Marija
Stefan
Aleksandar
Koj rodenden e potrebno da se prebara?

Marija

Rodendenot na Marija e na 17/01/1991
"""

birthdays = {"Ana": "13/03/1999", "Marija": "17/01/1991", "Stefan": "11/08/1996", "Aleksandar": "25/10/1992"}
print("Dobredojdovte vo recnikot za rodendeni. Nie gi znaeme rodendenite na:")
for (name, birthday) in birthdays.items():
    print(name)
print("Koj rodenden e potrebno da se prebara?")
name = input()
print(birthdays[name])

