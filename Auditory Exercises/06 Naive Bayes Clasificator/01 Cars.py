import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset


if __name__ == "__main__":
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = CategoricalNB()
    train_x_enc = encoder.transform(train_x)
    test_x_enc = encoder.transform(test_x)

    classifier.fit(train_x_enc, train_y)

    # Klasa predvidena za modelot
    pred_class_test_0 = classifier.predict([test_x_enc[0]])[0]

    # Vistinska klasa
    gt_class_test_0 = test_y[0]

    print(f'Vistinskata klasa za prviot test primerok: {gt_class_test_0}')
    print(f'Predvidenata klasa za prviot test primerok: {pred_class_test_0}')

    accuracy_count = 0

    for sample_x, gt_class in zip(test_x_enc, test_y):
        pred_class = classifier.predict([sample_x])[0]
        if gt_class == pred_class:
            accuracy_count += 1

    accuracy = accuracy_count / len(test_set)
    print(f'Tocnost na klasifikatorot: {accuracy}')

    entry = input().split(",")
    sample = encoder.transform([entry])
    predicted_class = classifier.predict(sample)[0]
    probabilities = classifier.predict_proba(sample)

    print(predicted_class)
    print(probabilities)
