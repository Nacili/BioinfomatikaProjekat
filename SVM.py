import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import  SVC
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def SVM(data):
    df = pd.read_csv(data)
    features1 = df.columns[1:2].tolist()
    features2 = df.columns[6:].tolist()
    features = features1 + features2

    x=df[features]
    x.columns = features
    y=df["sample"]

    x = pd.DataFrame(MinMaxScaler().fit_transform(x))
    x.columns = features
    print(x.head())

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # Parametri za unakrsnu validacuju
    parameters = [{'C': [pow(2,x) for x in range(-6,10,2)],
                         'kernel' : ['linear']
                         },

                  {'C': [pow(2,x) for x in range(-6,10,2)],
                         'kernel': ['poly'],
                         'degree': [2, 3, 4, 5],
                         'gamma': np.arange(0.1, 1.1, 0.1),
                         'coef0': np.arange(0, 2, 0.5)
                         },

                    {'C': [pow(2,x) for x in range(-6,10,2)],
                           'kernel' : ['rbf'],
                           'gamma': np.arange(0.1, 1.1, 0.1),
                           },

                   {'C': [pow(2,x) for x in range(-6,10,2)],
                          'kernel' : ['sigmoid'],
                          'gamma': np.arange(0.1, 1.1, 0.1),
                          'coef0': np.arange(0, 2, 0.5)
                          }]


    clf = GridSearchCV(SVC(), parameters, cv=5, scoring='f1_macro')
    clf.fit(x_train, y_train)

    print()
    print("Ocena uspeha po klasifikatorima:")
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) za %s" % (mean, std * 2, params))
        print()

    print("Najbolji parametri:")
    print(clf.best_params_)

    print(clf.best_estimator_.classes_)
    print('Broj podrzavajucih vektora', clf.best_estimator_.n_support_)

    print("Izvestaj za trening skup:")
    y_true, y_pred = y_train, clf.predict(x_train)
    print(classification_report(y_true, y_pred))
    print()

    print("Izvestaj za test skup:")
    y_true, y_pred = y_test, clf.predict(x_test)
    print(classification_report(y_true, y_pred))
    print()


