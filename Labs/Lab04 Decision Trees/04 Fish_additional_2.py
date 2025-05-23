"""
Во оваа верзија потребно е да се прави класификација дали примерокот припаѓа на класата Perch или не.
Променете го класниот атрибут така што на сите примероци кои припаѓаат
во класа различна од Perch ќе им биде доделена класа Not Perch.
За тренирање користете ги првите 85% од секоја од класите од податочното множество,
а за евалуација останатите 15% од секоја од класите.
Скалирајте го податочното множество со StandardScaler.
Потоа испечатете точност, предвидена класа за новиот примерок и добиените веројатности.

Input:
1
10
entropy
10 21 32 50 40 10

Result:
Tochnost so skalirani podatoci: 0.72
Predvidena klasa so skalirani podatoci: Not Perch
Verojatnosti: [1. 0.]
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script_2 import dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    col_index = int(input())
    trees = int(input())
    criterion = input()
    sample = input().split(" ")
    sample = sample[:col_index] + sample[(col_index + 1):]
    data = [row[:col_index] + row[(col_index + 1):] for row in dataset]

    perch = [row for row in data if row[-1] == "Perch"]
    not_perch = [row for row in data if row[-1] != "Perch"]

    threshold_perch = int(0.85 * len(perch))
    threshold_not_perch = int(0.85 * len(not_perch))

    train_set = perch[:threshold_perch] + not_perch[:threshold_not_perch]
    train_x = [row[:-1] for row in train_set]
    train_y = ["Perch" if row[-1] == "Perch" else "Not Perch" for row in train_set]

    test_set = perch[threshold_perch:] + not_perch[threshold_not_perch:]
    test_x = [row[:-1] for row in test_set]
    test_y = ["Perch" if row[-1] == "Perch" else "Not Perch" for row in test_set]

    standard_scaler = StandardScaler()
    standard_scaler.fit(train_x)

    classifier = RandomForestClassifier(n_estimators=trees, criterion=criterion, random_state=0)
    classifier.fit(standard_scaler.transform(train_x), train_y)

    predictions = classifier.predict(standard_scaler.transform(test_x))
    accuracy = accuracy_score(test_y, predictions)
    predicted_class = classifier.predict(standard_scaler.transform([sample]))[0]
    predictions = classifier.predict_proba(standard_scaler.transform([sample]))

    print(f"Tochnost so skalirani podatoci: {accuracy}")
    print(f"Predvidena klasa so skalirani podatoci: {predicted_class}")
    print(f"Verojatnosti: {predictions[0]}")


"""
1
10
entropy
10 21 32 50 40 10

1
10
gini
10 21 32 50 40 10

1
100
entropy
10 21 32 50 40 10

1
100
gini
10 21 32 50 40 10

5
10
entropy
10 21 32 50 40 10

5
10
gini
10 21 32 50 40 10

5
100
entropy
10 21 32 50 40 10

5
100
gini
10 21 32 50 40 10

3
150
entropy
10 21 32 50 40 10

3
150
gini
10 21 32 50 40 10
"""
