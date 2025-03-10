"""
Дефинирајте речник students во кој ќе се чуваат информации за предметите кои ги полагале студентите.
Од стандарден влез се читаат информации за име, презиме, број на индекс, предмет,
поени од теоретски дел, поени од практичен дел и поени од лабораториски вежби.
Може да се вчитаат информации за неограничен број студенти.
Вчитувањето информации завршува кога ќе се прочита клучниот збор end.
Пополнете го речникот students со вчитаните информации.
Потоа, за секој од студентите да се испечати името и презимето, и оцената за секој од предметите кои ги има полагано.

Оцената се пресметува на следниот начин:
[0, 50] - 5
(50, 60] - 6
(60, 70] - 7
(70, 80] - 8
(80, 90] - 9
(90, 100] - 10
"""


def grade(theory, practical, labs):
    total = int(theory) + int(practical) + int(labs)
    if 0 <= total <= 50:
        return 5
    elif total <= 60:
        return 6
    elif total <= 70:
        return 7
    elif total <= 80:
        return 8
    elif total <= 90:
        return 9
    else:
        return 10


if __name__ == "__main__":
    students = {}
    info = input()
    while info != "end":
        name, surname, index, subject, theory, practical, labs = info.split(",")
        if index not in students:
            students[index] = {"name": name, "surname": surname, "subjects": {}}
        students[index]["subjects"][subject] = grade(theory, practical, labs)
        info = input()

    for (index, student) in students.items():
        print("Student:", student["name"], student["surname"])
        for (subject, grade) in students[index]["subjects"].items():
            print(f"----{subject}: {grade}")
        print()
