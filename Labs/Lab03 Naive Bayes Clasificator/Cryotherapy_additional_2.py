"""
Во оваа верзија направете втора верзија од тренирачкото множество во која ќе ги додадете
погрешно класифицираните примероци од тестирачкото множество.
Овие примероци отстранете ги од тестирачкото множество.
Потоа направете и втор класификатор.
Вториот класификатор тренирајте го со втората верзија од тренирачкото множество,
а точноста пресметајте ја со тестирачкото множество.
На стандарден излез испечатете ја неговата точност.
Потоа испечатете ја предвидената класа на следниот начин:
ако со двата класификатори се добива истата класа да се испечати класата на стандарден излез,
во спротивно да се испечати „Klasata ne moze da bide odredena“.

Input:
1 20 4 3 1 6

Result:
Tochnost 1: 0.9285714285714286
Tochnost 2: 1.0
Predvidena klasa: 1
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script_2 import dataset

from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    dataset = [[float(x) for x in row] for row in dataset]

    threshold = int(0.85 * len(dataset))

    train_set = dataset[:threshold]
    train_x = [row[:-1] for row in train_set]
    train_y = [int(row[-1]) for row in train_set]

    test_set = dataset[threshold:]
    test_x = [row[:-1] for row in test_set]
    test_y = [int(row[-1]) for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)

    accuracy = 0

    for (y, prediction) in zip(test_y, predictions):
        if prediction == y:
            accuracy += 1
    accuracy = accuracy / len(test_y)
    print("Tochnost 1:", accuracy)

    # --------------------------------------------------
    train2 = train_set
    test2 = []

    for i, (y, prediction) in enumerate(zip(test_y, predictions)):
        if prediction == y:
            test2.append([*test_x[i], y])
        else:
            train2.append([*test_x[i], y])

    classifier2 = GaussianNB()

    train_x2 = [row[:-1] for row in train2]
    train_y2 = [int(row[-1]) for row in train2]

    test_x2 = [row[:-1] for row in test2]
    test_y2 = [int(row[-1]) for row in test2]

    classifier2.fit(train_x2, train_y2)

    predictions2 = classifier2.predict(test_x2)

    accuracy = 0

    for (y, prediction) in zip(test_y2, predictions2):
        if prediction == y:
            accuracy += 1
    accuracy = accuracy / len(test_y2)
    print("Tochnost 2:", accuracy)
    # --------------------------------------------------

    entry = [float(x) for x in input().split()]

    predicted_class1 = classifier.predict([entry])[0]
    probabilities = classifier.predict_proba([entry])

    predicted_class2 = classifier2.predict([entry])[0]

    if predicted_class1 == predicted_class2:
        print("Predvidena klasa:", predicted_class1)
    else:
        print("Klasata ne moze da bide odredena")

    submit_train_data(train_x, train_y)
    submit_second_train_data(train_x2, train_y2)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)
    submit_second_classifier(classifier2)
