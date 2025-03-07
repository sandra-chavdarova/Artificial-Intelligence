"""
Напишете програма која бара од корисникот да внесе име и години и потоа пресметува во која година тој ќе има 100 години.
Испечатете го неговото име и годината добиена.

Vnesete ime i godini:
Dimitar 23
Dimitar ke ima 100 godini vo 2097
"""

print("Vnesete ime i godini:")
name = input()
age = int(input())
print(name, "kje ima 100 godini vo", 2025 - age + 100)

