"""
Во оваа задача треба да направите класификација со колекција од 3 класификатори.
Тренирачкото множество поделете го на 3 дела така што првиот дел ќе ги содржи првите 3 карактеристики,
вториот дел ќе ги содржи вторите 3 карактеристики и третиот дел ќе ги содржи останатите 4 карактеристики
Потоа тренирајте 3 класификатори на следниот начин: првиот класификатор со првиот дел од тренирачкото множество,
вториот класификатор со вториот дел од тренирачкото множество и третиот класификатор со третиот дел од тренирачкото множество.
Пресметајте заедничка точност со тестирачкото множество.
Одреден примерок се смета за точно класифициран ако барем 2 од 3те класификатори точно ја предвидат класата.
За примерокот кој се чита од стандарден влез испечатете ја предвидената класа
само ако барем 2 од класификаторите ја предвидат истата класа.
Во спротивно испечатете „klasata ne moze da bide odredena“.

Input:
H R X 1 2 1 1 2 1 1

Result:
0.846820809248555
0
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script_1 import dataset

from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    threshold = int(0.75 * len(dataset))

    X = [row[:-1] for row in dataset]
    X = encoder.transform(X)
    dataset = [[*row_x, row[-1]] for row_x, row in zip(X, dataset)]

    train_set = dataset[:threshold]

    train_x1 = [row[:3] for row in train_set]
    train_x2 = [row[3:6] for row in train_set]
    train_x3 = [row[6:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    # encoder.fit(train_x1, train_x2, train_x3)

    test_set = dataset[threshold:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    # train_x_enc1 = encoder.transform(train_x1)
    # train_x_enc2 = encoder.transform(train_x2)
    # train_x_enc3 = encoder.transform(train_x3)

    # test_x_enc = encoder.transform(test_x)

    classifier1 = CategoricalNB()
    classifier2 = CategoricalNB()
    classifier3 = CategoricalNB()
    classifier1.fit(train_x1, train_y)
    classifier2.fit(train_x2, train_y)
    classifier3.fit(train_x3, train_y)

    accuracy = 0
    for x, y in zip(test_x, test_y):
        local_accuracy = 0
        pred1 = classifier1.predict([x[:3]])[0]
        pred2 = classifier2.predict([x[3:6]])[0]
        pred3 = classifier3.predict([x[6:]])[0]
        if pred1 == y:
            local_accuracy += 1
        if pred2 == y:
            local_accuracy += 1
        if pred3 == y:
            local_accuracy += 1

        if local_accuracy >= 2:
            accuracy += 1
    accuracy = accuracy / len(test_y)
    print(accuracy)

    entry = input().split(" ")
    sample = encoder.transform([entry])

    predicted_class1 = classifier1.predict([sample[0][:3]])[0]
    predicted_class2 = classifier2.predict([sample[0][3:6]])[0]
    predicted_class3 = classifier3.predict([sample[0][6:]])[0]
    local = 0
    if predicted_class1 == predicted_class2:
        print(predicted_class1)
    elif predicted_class1 == predicted_class3:
        print(predicted_class1)
    elif predicted_class2 == predicted_class3:
        print(predicted_class2)
    else:
        print("Klasata ne moze da bide odredena")
