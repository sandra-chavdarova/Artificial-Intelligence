"""
Напишете функција која ќе ги содржи функционалностите на едноставен аритметички калкулатор.
Интеракција со калкулаторот треба да се врши преку читање на параметри од стандардниот влез со наредбата input(),
т.е. се внесуваат двата операнди и операторот во командна линија.
По процесирање на барањето од страна на функцијата се обработува и се печати резултатот на екран.
Командите кои ги испраќаме на калкулаторот се читаат од стандарден влез и треба да го имаат следниот формат:
операнд1
оператор
операнд2
Доколку настанала грешка при внес да се извести корисникот со соодветна порака. Калкулаторот треба да ги поддржува следните операции:
Собирање (+)
Одземање (-)
Множење (*)
Целобројно делење (//)
Делење (/)
Модуло (остаток) (%)
Степенување (**)
"""


def calculator(x, operator, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    elif operator == "//":
        return x // y
    elif operator == "**":
        return x ** y
    elif operator == "%":
        return x % y
    else:
        return "Error"


if __name__ == "__main__":
    x = float(input())
    operator = input()
    y = float(input())
    result = calculator(x, operator, y)
    print("Result:", result)

