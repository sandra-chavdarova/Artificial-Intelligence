"""
Напишете програма која на влез прима два броја и проверува дали првиот број е делив со вториот.
Да се испечати 'Deliv' ако е делив.

Vnesete dva broj:
125
5
Deliv
"""

print("Vnesete dva broja")
a = int(input())
b = int(input())
if a % b == 0:
    print("Deliv")
else:
    print("Ne e deliv")
