"""
Користејќи list comprehension дадена матрица составена од броеви да се промени секој елемент така што
ако припаѓа во горната половина(индексот на редицата е помеѓу 0 и n/2) треба да се помножи со 2,
а ако припаѓа на долната половина треба да се помножи со 3.
Секој елемент на матрицата се чита од тастатура така што прво се читаат N и M (број на редици и колони),
а потоа во секој ред се читаат елементите одделени со празно место.

Пример влез:
4
4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Излез: [[2, 4, 6, 8], [2, 4, 6, 8], [3, 6, 9, 12], [3, 6, 9, 12]]
"""

n = int(input())
m = int(input())
result = []
for i in range(n):
    row = [int(element) for element in input().split(" ")]
    if i < n / 2:
        result.append([item * 2 for item in row])
    else:
        result.append([item * 3 for item in row])
print(result)
