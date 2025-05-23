"""
Дадено ни е податочно множество за соларен одблесок. Сите атрибути кои ги содржи се од категориски тип.
Ваша задача е да истренирате класификатор - дрво на одлука кој ќе предвидува класи на соларен одблесок
користејќи ги последните X% од даденото податочно множество.
Треба да ја пресметате точноста која ја добивате над останатите (100 - X)% од податочното множество.

Во почетниот код имате дадено податочно множество. На влез се прима вредност за процентот на поделба X.
На пример, ако вредноста е 80 значи дека ги користите последните 80% од множеството за тренирање, а првите 20% за тестирање.
Дополнително во променливата criterion се вчитува вредност за критериумот за избор на најдобар атрибут.

На излез треба да се испечати точност, длабочина и број на листови на изграденото дрво,
како и карактеристиките со најголема и најмала важност.

За да ги добиете истите резултати како и во тест примерите,
при креирање на класификаторот поставете random_state=0.

Input:
50
entropy

Result:
Depth: 12
Number of leaves: 125
Accuracy: 0.7771345875542692
Most important feature: 0
Least important feature: 9
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script_1 import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    data = dataset
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in data])

    threshold = int(input())
    criterion = input()
    threshold = int((100 - threshold) * len(data) / 100)

    train_set = data[threshold:]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = data[:threshold]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(train_x, train_y)

    print(f"Depth: {classifier.get_depth()}")
    print(f"Number of leaves: {classifier.get_n_leaves()}")

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)
    print(f"Accuracy: {accuracy}")
    feature_importances = [float(x) for x in classifier.feature_importances_]
    print(f"Most important feature: {feature_importances.index(max(feature_importances))}")
    print(f"Least important feature: {feature_importances.index(min(feature_importances))}")

    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)
    submit_encoder(encoder)
