"""
Напишете програма каде корисникот внесува број и на екран му се печати
'Paren' ако бројот е парен или 'Neparen' ако бројот е непарен.
Дополнително ако бројот е делив со 4 да се испечати 'Deliv so 4'

Vnesete broj:
8
Paren
Deliv so 4
"""

print("Vnesete broj")
a = int(input())
if a % 2 == 0:
    print("Paren")
else:
    print("Neparen")
if a % 4 == 0:
    print("Deliv so 4")
else:
    print("Ne e deliv so 4")
