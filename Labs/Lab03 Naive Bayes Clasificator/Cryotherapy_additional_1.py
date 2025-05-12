"""
Во оваа верзија користете ги последните 85% (прв дел) од податочното множество за тренирање, а останатите 15% (втор дел) за евалуација.
Потоа направете и втор класификатор. Вториот класификатор тренирајте го со вториот дел од податочното множество,
а точноста пресметајте ја со првиот дел. На стандарден излез испечатете ја неговата точност.
Потоа испечатете ја предвидената класа на следниот начин:
ако со двата класификатори се добива истата класа да се испечати класата на стандарден излез,
во спротивно да се испечати „Klasata ne moze da bide odredena“.

Input:
1 20 4 3 1 6

Result:
Tochnost 1: 0.8461538461538461
Tochnost 2: 0.7837837837837838
Klasata ne moze da bide odredena
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script_2 import dataset

from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    dataset = [[float(x) for x in row] for row in dataset]

    threshold = int(0.15 * len(dataset))

    train_set = dataset[threshold:]
    train_x = [row[:-1] for row in train_set]
    train_y = [int(row[-1]) for row in train_set]

    test_set = dataset[:threshold]
    test_x = [row[:-1] for row in test_set]
    test_y = [int(row[-1]) for row in test_set]

    classifier1 = GaussianNB()
    classifier1.fit(train_x, train_y)

    predictions = classifier1.predict(test_x)

    accuracy = 0
    for (y, prediction) in zip(test_y, predictions):
        if prediction == y:
            accuracy += 1
    accuracy = accuracy / len(test_y)
    print("Tochnost 1:", accuracy)
    # ---------------------------------------
    train_set = dataset[:threshold]
    train_x = [row[:-1] for row in train_set]
    train_y = [int(row[-1]) for row in train_set]

    test_set = dataset[threshold:]
    test_x = [row[:-1] for row in test_set]
    test_y = [int(row[-1]) for row in test_set]

    classifier2 = GaussianNB()
    classifier2.fit(train_x, train_y)

    predictions = classifier2.predict(test_x)

    accuracy = 0
    for (y, prediction) in zip(test_y, predictions):
        if prediction == y:
            accuracy += 1
    accuracy = accuracy / len(test_y)
    print("Tochnost 2:", accuracy)

    entry = [float(x) for x in input().split()]
    predicted_class1 = classifier1.predict([entry])[0]
    predicted_class2 = classifier2.predict([entry])[0]
    print(predicted_class1, predicted_class2)

    if predicted_class1 == predicted_class2:
        print("Predvidena klasa:", predicted_class1)
    else:
        print("Klasata ne moze da bide odredena")
