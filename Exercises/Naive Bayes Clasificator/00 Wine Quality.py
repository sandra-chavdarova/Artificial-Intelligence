"""
Дадено е податочно множество за класификација на квалитет на вино.
Секоја инстанца е претставена со 11 хемиски карактеристики и една класа за добар ('good') и лош ('bad') квалитет на вино.
Променете го податочното множество така што првата и последната хемиска карактеристика ќе ги замените со збирот на соодветните вредности.
Новата карактеристика поставете ја како прва колона во множеството.
Новата верзија на податочното множество треба да има 10 хемиски карактеристики.

Поделете го податочното множество на множества за тренирање и тестирање на следниот начин.
Ако критериумот за поделба C има вредност 0 за тренирање се користат првите P проценти од секоја од класите, а за тестирање останатите 100 - P проценти.
Ако критериумот за поделба C има вредност 1 за тренирање се користат последните P проценти од секоја од класите, а за тестирање останатите 100 - P проценти.
При поделба користете ја прво класата good, а потоа класата bad.
Потоа скалирајте ги атрибутите во рангот [-1, 1].

Направете наивен баесов класификатор кој ќе го тренирате со верзијата на податочното множество
во која првата и последната хемиска карактеристика се заменети со нивниот збир без примена на скалирање.
Потоа, направете и втор наивен баесов класификатор кој ќе го тренирате со верзијата на податочното множество
во која првата и последната хемиска карактеристика се заменети со нивниот збир и потоа е применето скалирање.
Испечатете ја точноста на двата класификатори.

Од стандарден влез прво се чита критериумот за поделба C, а потоа се чита процентот за поделба P.

На стандарден излез да се испечати точноста добиена со двата класификатори.

Input:
0
70

Results:
Broj na podatoci vo train se: 1118
Broj na podatoci vo test se: 481
Tochnost so zbir na koloni: 0.6694386694386695
Tochnost so zbir na koloni i skaliranje: 0.6881496881496881
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.metrics import accuracy_score
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    global dataset
    C = int(input())
    P = int(input())

    new_dataset = list()
    for row in dataset:
        new_row = list()
        new_row.append(row[0] + row[-2])
        new_row.extend(row[1:-2])
        new_row.append(row[-1])
        new_dataset.append(new_row)
    data = new_dataset

    good = [row for row in data if row[-1] == "good"]
    bad = [row for row in data if row[-1] == "bad"]

    good_count = len(good)
    bad_count = len(bad)

    if C == 0:
        good_threshold = int(P / 100 * good_count)
        bad_threshold = int(P / 100 * bad_count)

        train_set = good[:good_threshold] + bad[:bad_threshold]
        test_set = good[good_threshold:] + bad[bad_threshold:]
    else:
        good_threshold = int((100 - P) / 100 * good_count)
        bad_threshold = int((100 - P) / 100 * bad_count)

        train_set = good[good_threshold:] + bad[bad_threshold:]
        test_set = good[:good_threshold] + bad[:bad_threshold]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)
    print(f"Broj na podatoci vo train se: {len(train_set)}")
    print(f"Broj na podatoci vo test se: {len(test_set)}")
    print(f"Tochnost so zbir na koloni: {accuracy}")

    min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
    min_max_scaler.fit(train_x)
    classifier.fit(min_max_scaler.transform(train_x), train_y)
    predictions = classifier.predict(min_max_scaler.transform(test_x))
    accuracy = accuracy_score(test_y, predictions)
    print(f"Tochnost so zbir na koloni i skaliranje: {accuracy}")
