"""
Дадено ни е податочно множество за карактеристики на риби. Сите атрибути кои ги содржи се од непрекинат тип.
Ваша задача е да истренирате класификатор - колекција од дрва на одлука кој ќе предвидува класи на тип на риби
користејќи ги првите 85% од даденото податочно множество.
Треба да ја пресметате точноста која ја добивате над останатите 15% од податочното множество.
Притоа, се користи дел од множеството во кој е отстранета колоната col_index.

Во почетниот код имате дадено податочно множество.
На влез се прима индекс на колоната која треба да се отстрани col_index.
Дополнително се вчитува бројот на дрва на одлука кои ќе се користат и вредност за критериумот за избор на најдобар атрибут.
На крај, се вчитува нов запис кој треба да се класифицира со тренираниот класификатор.

На излез треба да се испечати точност на класификаторот, предвидената класа за новиот запис и веројатностите за припадност во класите.

Напомена: бидејќи вредностите се од непрекинат тип, нема потреба да ги претворите во целобројни вредности.

За да ги добиете истите резултати како и во тест примерите, при креирање на класификаторот поставете random_state=0.

Input:
1
10
entropy
10 21 32 50 40 10

Result:
Accuracy: 0.7916666666666666
Bream
[0.6 0.  0.2 0.  0.1 0.1 0. ]
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script_2 import dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    col_index = int(input())
    trees = int(input())
    criterion = input()
    sample = input().split(" ")
    sample = sample[:col_index] + sample[(col_index + 1):]
    data = [row[:col_index] + row[(col_index + 1):] for row in dataset]
    threshold = int(0.85 * len(data))

    train_set = data[:threshold]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = data[threshold:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=trees, criterion=criterion, random_state=0)
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)
    print(f"Accuracy: {accuracy}")
    predicted_class = classifier.predict([sample])[0]
    print(predicted_class)
    predictions = classifier.predict_proba([sample])
    print(predictions[0])

    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)
