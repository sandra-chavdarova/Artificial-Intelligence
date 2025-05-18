"""
Креирајте модел на невронска мрежа за класификација на квалитет на вино. Податочното множество е зададено во датотеката winequality.csv.
Секоја инстанца е претставена со 11 хемиски карактеристики и една класа за добар ('good') и лош ('bad') квалитет на вино.

Потребно е податочното множество да се подели на тренирачко, валидациско и тестирачко множество,
така што првите 70% (како што се појавуваат во податочното множество) од секоја од класите да се доделат во тренирачкото множество.
Следните 10% од секоја од класите влегуваат во валидациско множество, а последните 20% се дел од тестирачкото множество.

Со помош на валидациското множество изберете го најдобриот број на неврони во скриениот слој од можностите [5, 10, 100].
Моделот со најдобра точност со валидациското множество потребно е да се искористи како финален модел.
Моделите се тренираат со рата на учење од 0.001, 500 епохи и ReLU активациска функција на невроните од скриениот слој.
Финалниот модел потребно е да се евалуира со тестирачкото множество и да се пресмета точноста на моделот.
"""

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])
    return data


if __name__ == '__main__':
    dataset = read_dataset()
    dataset_good = [row for row in dataset if row[-1] == "good"]
    dataset_bad = [row for row in dataset if row[-1] == "bad"]

    train_set = dataset_bad[:int(0.7 * len(dataset_bad))] + dataset_good[:int(0.7 * len(dataset_good))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_set = dataset_bad[int(0.7 * len(dataset_bad)):int(0.8 * len(dataset_bad))] + \
              dataset_good[int(0.7 * len(dataset_good)):int(0.8 * len(dataset_good))]
    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    test_set = dataset_bad[int(0.8 * len(dataset_bad)):] + dataset_good[:int(0.8 * len(dataset_good)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier1 = MLPClassifier(5, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier1.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)

    predictions1 = classifier1.predict(val_x)
    predictions2 = classifier2.predict(val_x)
    predictions3 = classifier3.predict(val_x)

    accuracy1 = accuracy_score(val_y, predictions1)
    accuracy2 = accuracy_score(val_y, predictions2)
    accuracy3 = accuracy_score(val_y, predictions3)

    print(f"Tochnost so 5 nevroni nad validacisko mnozestvo: {accuracy1}")
    print(f"Tochnost so 10 nevroni nad validacisko mnozestvo: {accuracy2}")
    print(f"Tochnost so 100 nevroni nad validacisko mnozestvo: {accuracy3}")

    if accuracy1 >= accuracy2 and accuracy1 >= accuracy3:
        predictions = classifier1.predict(test_x)
        accuracy = accuracy_score(test_y, predictions)
        print(f"Tochnost so testirachko mnozestvo: {accuracy}")
    elif accuracy2 >= accuracy1 and accuracy2 >= accuracy3:
        predictions = classifier2.predict(test_x)
        accuracy = accuracy_score(test_y, predictions)
        print(f"Tochnost so testirachko mnozestvo: {accuracy}")
    else:
        predictions = classifier3.predict(test_x)
        accuracy = accuracy_score(test_y, predictions)
        print(f"Tochnost so testirachko mnozestvo: {accuracy}")
