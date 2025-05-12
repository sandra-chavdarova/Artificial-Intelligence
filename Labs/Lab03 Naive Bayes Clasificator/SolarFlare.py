"""
Дадено ни е податочно множество за соларен одблесок.
Сите атрибути кои ги содржи се од категориски тип (последната колона е класен атрибут).
Ваша задача е да истренирате наивен баесов класификатор кој ќе предвидува класи на соларен одблесок
користејќи ги првите 75% од даденото податочно множество.
Треба да ја пресметате точноста која ја добивате над останатите 25% од податочното множество
и потоа да направите предвидувања на записи кои ги примате на влез.

Во почетниот код имате дадено податочно множество.
На влез се прима еден запис за кој треба да се направи предвидување на класата.
На излез треба да се испечати точноста на моделот, класата на предвидување како и веројатностите за припадност во класите.

Input:
H R X 1 2 1 1 2 1 1

Result:
0.8294797687861272
0
[[9.94855050e-01 4.57710457e-03 3.71407825e-04 9.29521929e-05
  3.34611214e-05 3.36218889e-05 7.71205438e-06 2.86906785e-05]]
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script_1 import dataset

from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    encoder = OrdinalEncoder()

    threshold = int(0.75 * len(dataset))

    train_set = dataset[:threshold]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    encoder.fit(train_x)

    test_set = dataset[threshold:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    train_x_enc = encoder.transform(train_x)
    test_x_enc = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x_enc, train_y)

    accuracy = 0
    for (x, y) in zip(test_x_enc, test_y):
        prediction = classifier.predict([x])[0]
        if prediction == y:
            accuracy += 1
    accuracy = accuracy / len(test_y)
    print(accuracy)

    entry = input().split(" ")
    sample = encoder.transform([entry])

    predicted_class = classifier.predict(sample)[0]
    probabilities = classifier.predict_proba(sample)

    print(predicted_class)
    print(probabilities)

    submit_train_data(train_x_enc, train_y)
    submit_test_data(test_x_enc, test_y)
    submit_classifier(classifier)
    submit_encoder(encoder)
