import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.neighbors import  KNeighborsClassifier
import sklearn.preprocessing as prep


def KNeighbors(data):
    #ucitavanje
    df = pd.read_excel(data)
    features = df.columns[:4].tolist()
    x_original=df[features]

    features1 = df.columns[1:2].tolist()
    features2 = df.columns[6:].tolist()
    features = features1 + features2

    #normalizacija
    x_original=df[features]
    x=pd.DataFrame(prep.MinMaxScaler().fit_transform(x_original))
    x.columns = features
    y=df["sample"]

    #podela na trening i test skup
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.95, stratify=y)

    # Parametri za unakrsnu validacuju
    parameters = [{'n_neighbors': range(3,10),
                   'p':[1, 2],
                   'weights': ['uniform', 'distance'],
                   }]

    scores = ['precision', 'f1']

    for score in scores:
        print("Mera ", score)
        print()
    clf = GridSearchCV(KNeighborsClassifier(), parameters, cv=5, scoring='%s_macro' % score)
    clf.fit(x_train, y_train)

    #rezultati
    print("Najbolji parametri:")
    print(clf.best_params_)
    print()
    print("Ocena uspeha po klasifikatorima:")
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) za %s" % (mean, std * 2, params))
    print()

    print("Izvestaj za test skup:")
    y_true, y_pred = y_test, clf.predict(x_test)
    print(classification_report(y_true, y_pred))
    print()
