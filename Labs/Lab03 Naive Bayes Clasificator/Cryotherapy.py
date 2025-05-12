"""
Дадено ни е податочно множество за третмани со криотерапија.
Сите атрибути кои ги содржи се од непрекинат тип и може да се претпостави дека имаат непрекината распределба.
Ваша задача е да истренирате наивен баесов класификатор кој ќе предвидува дали терапијата е успешна или не (1 и 0)
користејќи ги првите 85% од даденото податочно множество.
Треба да ја пресметате точноста која ја добивате над останатите 15% од податочното множество
и потоа да направите предвидувања на записи кои ги примате на влез.

Во почетниот код имате дадено податочно множество.
На влез се прима еден запис за кој треба да се направи предвидување на класата.
На излез треба да се испечати точноста на моделот, класата на предвидување како и веројатностите за припадност во класите.

Input:
1 20 4 3 1 6

Result:
0.9285714285714286
1
[[0.0025448 0.9974552]]
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
    print(accuracy)

    entry = [float(x) for x in input().split()]
    # entry = input().split()

    predicted_class = classifier.predict([entry])[0]
    probabilities = classifier.predict_proba([entry])

    print(predicted_class)
    print(probabilities)

    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)

