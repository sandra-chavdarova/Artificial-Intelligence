import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset


if __name__ == '__main__':
    dataset = read_file('car.csv')
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    threshold = int(0.7 * len(dataset))
    train_set = dataset[:threshold]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[threshold:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = RandomForestClassifier(n_estimators=150, criterion="entropy", random_state=0)
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)
    print(f"Accuracy: {accuracy}")

    # feature_importances = list(classifier.feature_importances_)
    feature_importances = [float(x) for x in classifier.feature_importances_]
    print(f"Feature importances: {feature_importances}")

    most_important_feature = feature_importances.index(max(feature_importances))
    least_important_feature = feature_importances.index(min(feature_importances))
    print(f"Most important feature: {most_important_feature}")
    print(f"Least important feature: {least_important_feature}")
