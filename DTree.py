import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import tree
from sklearn.metrics import classification_report 


def DTree(data):
    #ucitavanje
    df = pd.read_excel(data)
    features = df.columns[:4].tolist()

    features1 = df.columns[1:2].tolist()
    features2 = df.columns[6:].tolist()
    features = features1 + features2
    
    x=df[features]
    y=df["sample"]

    #podela na trening i test skup
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, shuffle=True)
    
    # Parametri za unakrsnu validacuju
    parameters = [{'criterion': ['entropy', 'gini'],
                   'max_depth':[5,  12, 20]
                   }]
    
    #unakrsna validacija i građenje drveta
    clf = GridSearchCV(tree.DecisionTreeClassifier(), parameters, cv=5)
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
