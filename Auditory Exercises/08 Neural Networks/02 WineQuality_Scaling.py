"""
Потребно е да се испита како скалирањето на карактеристиките допридонесува до подобрување на моделот од претходната задача.
Употребете ја истата поделба на податочните множества од претходната задача и креирајте модел кој се покажал како најдобар од претходната задача.
Потребно е моделот да се истренира со оригиналните податоци, со податоци кои се скалирани со StandardScaler, и со податоци скалирани со MinMaxScaler.
Со помош на валидациското множество одберете која техника е најдобриот начин за репрезентација на податоците,
па потоа соодветно направете евалуација на моделот со тестирачкото множество преку пресметување на точноста, прецизноста и одзивот.

точност = (TP + TN) / (TP + FP + TN + FN)
прецизност = TP / (TP + FP)
одзив = TP / (TP + FN)

TP - број на точно предвидени позитивни класи
FP - број на грешно предвидени позитивни класи
TN - број на точно предвидени негативни класи
FN - број на грешно предвидени негативни класи
"""

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score


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

    classifier1 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier1.fit(train_x, train_y)
    predictions1 = classifier1.predict(val_x)
    accuracy1 = accuracy_score(val_y, predictions1)
    print(f"Tochnost so originalno mnozestvo: {accuracy1}")

    standard_scaler = StandardScaler()
    standard_scaler.fit(train_x)

    classifier2 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2.fit(standard_scaler.transform(train_x), train_y)
    predictions2 = classifier2.predict(standard_scaler.transform(val_x))
    accuracy2 = accuracy_score(val_y, predictions2)
    print(f"Tochnost so normalizacija so StandardScaler: {accuracy2}")

    min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
    min_max_scaler.fit(train_x)

    classifier3 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3.fit(min_max_scaler.transform(train_x), train_y)
    predictions3 = classifier3.predict(min_max_scaler.transform(val_x))
    accuracy3 = accuracy_score(val_y, predictions3)
    print(f"Tochnost so normalizacija so MinMaxScaler (-1, 1): {accuracy3}")

    predictions = 0
    if accuracy1 >= accuracy2 and accuracy1 >= accuracy3:
        predictions = classifier1.predict(test_x)
    elif accuracy2 >= accuracy1 and accuracy2 >= accuracy3:
        predictions = classifier2.predict(test_x)
    else:
        predictions = classifier3.predict(test_x)

    accuracy = accuracy_score(test_y, predictions)
    precision = precision_score(test_y, predictions, pos_label="good")
    recall = recall_score(test_y, predictions, pos_label="good")
    print(f"Tochnost so testirachko mnozestvo: {accuracy}")
    print(f"Preciznost so testirachko mnozestvo: {precision}")
    print(f"Odziv so testirachko mnozestvo: {recall}")
