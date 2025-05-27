"""
Дадено е податочно множество за класификација на тип на риби.
Секоја инстанца е претставена со 6 карактеристики и една класа за типот на риба ('Perch', 'Roach', 'Bream').
Поделете го податочното множество на множества за тренирање и тестирањe така што
за тренирање се користат првите P проценти од множеството, а за тестирање останатите 100 - P проценти.

Потребно е да направите 2 класификатори за класификација на тип на риба:
- Дрво на одлука со критериум C за избор на најдобар атрибут и најмногу L листови.
- Колекција од 3 дрва на одлука со критериум C за избор на најдобар атрибут и најмногу L листови.
  Секое од овие 3 дрва на одлука има за цел класификација на еден тип на риба (една класа од податочното множество).
  На пример: 1 дрво на одлука има за цел да класифицира дали примерокот е од класата 'Roach' (1) или не (0).

Двата класификатори тренирајте ги со истата поделба на податочното множество.

Пресметајте ја точноста на двата класификатори. Точноста на вториот класификатор се пресметува на следниот начин.
Даден примерок се смета за точно класифициран доколку сите 3 класификатори имаат усогласено предвидување на точната класа.
На пример: ако за даден примерок точната класа е 'Roach', за примерокот да биде точно класифициран потребно е класификаторот
задолжен за класификација на класата 'Roach' да предвиди дека примерокот припаѓа во класата за која е задолжен,
а другите 2 класификатори да предвидат дека примерокот не припаѓа во класата за која е задолжен секој од двата класификатори соодветно.

Од стандарден влез прво се чита процентот за поделба P. Потоа се чита критериумот C за избор на најдобар атрибут,
и на крај се чита максималниот број на листови L за класификаторот.

На стандарден излез да се испечати точноста добиена со двата класификатори.

За да ги добиете истите резултати како и во тест примерите, при креирање на класификаторите поставете random_state=0.

Input:
70
gini
20

Result:
Tochnost so originalniot klasifikator: 0.7352941176470589
Tochnost so kolekcija od klasifikatori: 0.6764705882352942
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    P = int(input())
    criteria = input()
    L = int(input())
    threshold = int(P / 100 * len(dataset))

    train_set = dataset[:threshold]
    test_set = dataset[threshold:]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier1 = DecisionTreeClassifier(criterion=criteria, max_leaf_nodes=L, random_state=0)
    classifier1.fit(train_x, train_y)
    predictions1 = classifier1.predict(test_x)
    accuracy1 = accuracy_score(test_y, predictions1)

    classifiers = []
    for class_ in ["Perch", "Roach", "Bream"]:
        classifier = DecisionTreeClassifier(criterion=criteria, max_leaf_nodes=L, random_state=0)
        test_y_modified = [1 if label == class_ else 0 for label in train_y]
        classifier.fit(train_x, test_y_modified)
        classifiers.append((class_, classifier))

    count = 0
    for row_x, label in zip(test_x, test_y):
        flag = True
        for class_, classifier in classifiers:
            prediction = classifier.predict([row_x])[0]
            if label == class_:
                if prediction != 1:
                    flag = False
                    break
            else:
                if prediction != 0:
                    flag = False
                    break
        if flag:
            count += 1

    accuracy2 = count / len(test_y)
    print(f"Tochnost so originalniot klasifikator: {accuracy1}")
    print(f"Tochnost so kolekcija od klasifikatori: {accuracy2}")
