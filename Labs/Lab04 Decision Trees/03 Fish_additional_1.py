"""
Во оваа верзија направете втора верзија на податочното множество која ќе биде наменета
за одредување дали дадениот примерок претставува риба од типот Perch или не.
Направете втор класификатор кој ќе го тренирате со променетото множество.
Испечатете ја точноста на двата класификатори и предвидената класа за новиот примерок.

Input:
2
10
entropy
10 21 32 50 40 10

Result:
Tochnost so originalnoto mnozestvo: 0.7916666666666666
Tochnost so binarna klasifikacija: 0.7083333333333334
Predvidena klasa so originalnoto mnozestvo: Smelt
Predvidena klasa so binarna klasifikacija: 0
"""
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
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

    classifier1 = RandomForestClassifier(n_estimators=trees, criterion=criterion, random_state=0)
    classifier1.fit(train_x, train_y)

    predictions1 = classifier1.predict(test_x)
    accuracy1 = accuracy_score(test_y, predictions1)

    predicted_class1 = classifier1.predict([sample])[0]

    # ---------------------------------------------------------------------------------------------

    train_y = [1 if x == "Perch" else 0 for x in train_y]
    test_y = [1 if x == "Perch" else 0 for x in test_y]

    classifier2 = RandomForestClassifier(n_estimators=trees, criterion=criterion, random_state=0)
    classifier2.fit(train_x, train_y)

    predictions2 = classifier2.predict(test_x)
    accuracy2 = accuracy_score(test_y, predictions2)
    predicted_class2 = classifier2.predict([sample])[0]

    print(f"Tochnost so originalnoto mnozestvo: {accuracy1}")
    print(f"Tochnost so binarna klasifikacija: {accuracy2}")
    print(f"Predvidena klasa so originalnoto mnozestvo: {predicted_class1}")
    print(f"Predvidena klasa so binarna klasifikacija: {predicted_class2}")


"""
2
10
entropy
10 21 32 50 40 10

5
10
gini
10 21 32 50 40 10

0
100
entropy
10 21 32 50 40 10

0
100
gini
10 21 32 50 40 10

0
10
entropy
10 21 32 50 40 10

1
10
gini
10 21 32 50 40 10

4
100
entropy
10 21 32 50 40 10

0
100
gini
10 21 32 50 40 10

0
150
entropy
10 21 32 50 40 10

5
150
gini
10 21 32 50 40 10
"""
