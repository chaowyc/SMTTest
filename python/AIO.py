from time import time
from sklearn import linear_model
from RegressionBase import *
from sklearn import metrics
from sklearn.svm.classes import SVR

import csv, os


'''
target_names = ['class 1', 'class 0']
labels = [1, 0]
def benchmark(clf, name, X_train, y_train, X_test, y_test):
    print('_' * 80)
    print("Training: ")
    print(clf)
    t0 = time()
    clf.fit(X_train, y_train)
    train_time = time() - t0
    print("train time: %0.3fs" % train_time)

    t0 = time()
    pred = clf.predict(X_test)
    test_time = time() - t0
    print("test time:  %0.3fs" % test_time)

    pred, _, _ = RegressionBase.Timeout(pred, 1)
    Y_test, num0, num1 = RegressionBase.Timeout(y_test, 1)

    score = metrics.accuracy_score(Y_test, pred)
    print("accuracy:   %0.3f" % score)

    print("classification report:")
    print(metrics.classification_report(Y_test, pred,
                                        target_names=target_names, labels=labels))

    print("confusion matrix:")
    print(metrics.confusion_matrix(Y_test, pred))

    print()
    clf_descr = str(clf).split('(')[0]

    return pred, Y_test, num0, num1




train_file_list = []
test_file_list = []
X_train, y_train, X_test, y_test = '','','',''


for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        if os.path.splitext(fname)[1] == '.ml':
            # we can delete unneeded path information later when writing results to report file.
            # e.g. given "/home/jack/test/QF_BV/12434/test.smt2", keep only "QF_BV/12434/test.smt2"
            train_file_list.append(os.path.join(root, fname))
for root, dirs, files in os.walk(sys.argv[2]):
    for fname in files:
        if os.path.splitext(fname)[1] == '.csv_ml':
            test_file_list.append(os.path.join(root, fname))

train_file = ''
test_file = ''
for trainfile in train_file_list:
    train = os.path.basename(trainfile).split('.')[0].split('_')[1]
    for testfile in test_file_list:
        test = os.path.basename(testfile).split('.')[0]
        if  train==test :
            train_file = trainfile
            test_file = testfile
            rt = RegressionBase(train_file, test_file)
            X_train, y_train, X_test, y_test = rt.Test()
            print train_file, test_file
            output_file = sys.argv[3] + '/' + os.path.basename(test_file).split('.')[0] + '.csv'
            with open(output_file, 'w') as out:
                field_name = ["name", "class0", "TP0", "FP0", "FN0", "Precision0", "Recall0", "class1", "TP1", "FP1", "FN1", "Precision1", "Recall1"]
                writer = csv.DictWriter(out, fieldnames=field_name)
                writer.writeheader()
                output_dict = dict()
                for clf, name in (
                    (linear_model.LinearRegression(), "LinearRegression"),
                    (linear_model.Lasso(alpha=0.5), "LassoRegression"),
                    (linear_model.Ridge(alpha=0.5), "RidgeRegression"),
                    (linear_model.ElasticNet(alpha=0.5, l1_ratio=0.7), "ElasticNet")):
                    print('=' * 80)
                    print(name)
                    pred, act, num0, num1 = benchmark(clf, name, X_train, y_train, X_test, y_test)

                    p, r, f, s = precision_recall_fscore_support(y_true=np.array(act), y_pred=np.array(pred), average=None,
                                                                 sample_weight=None, labels=labels)
                    tp, fp, fn = RegressionBase.tp_fp_fn(pre_y=np.array(pred), act_y=np.array(act))
                    output_dict['name'] = name
                    output_dict["class0"] = num0
                    output_dict["TP0"] = tp[0]
                    output_dict["FP0"] = fp[0]
                    output_dict["FN0"] = fn[0]
                    output_dict["Precision0"] = "{0:0.{1}f}".format(p[1], 2)
                    output_dict["Recall0"] = "{0:0.{1}f}".format(r[1], 2)
                    output_dict["class1"] = num1
                    output_dict["TP1"] = tp[1]
                    output_dict["FP1"] = fp[1]
                    output_dict["FN1"] = fn[1]
                    output_dict["Precision1"] = "{0:0.{1}f}".format(p[0], 2)
                    output_dict["Recall1"] = "{0:0.{1}f}".format(r[0], 2)
                    writer.writerow(output_dict)
                    output_dict.clear()
'''

target_names = ['class 1', 'class 0']
labels = [1, 0]
def benchmark(clf, name, X_train, y_train, X_test, y_test):
    print('_' * 80)
    print("Training: ")
    print(clf)
    t0 = time()
    clf.fit(X_train, y_train)
    train_time = time() - t0
    print("train time: %0.3fs" % train_time)

    t0 = time()
    pred = clf.predict(X_test)
    test_time = time() - t0
    print("test time:  %0.3fs" % test_time)

    pred, _, _ = RegressionBase.Timeout(pred, 2)
    Y_test, num0, num1 = RegressionBase.Timeout(y_test, 2)

    score = metrics.accuracy_score(Y_test, pred)
    print("accuracy:   %0.3f" % score)

    print("classification report:")
    print(metrics.classification_report(Y_test, pred,
                                        target_names=target_names, labels=labels))

    print("confusion matrix:")
    print(metrics.confusion_matrix(Y_test, pred))

    print()
    clf_descr = str(clf).split('(')[0]

    return pred, Y_test, num0, num1




train_file_list = []
test_file_list = []
X_train, y_train, X_test, y_test = '','','',''


for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        if os.path.splitext(fname)[1] == '.ml':
            # we can delete unneeded path information later when writing results to report file.
            # e.g. given "/home/jack/test/QF_BV/12434/test.smt2", keep only "QF_BV/12434/test.smt2"
            train_file_list.append(os.path.join(root, fname))
for root, dirs, files in os.walk(sys.argv[2]):
    for fname in files:
        if os.path.splitext(fname)[1] == '.csv_ml':
            test_file_list.append(os.path.join(root, fname))





for clf, name in (
    (linear_model.LinearRegression(), "LinearRegression"),
    (linear_model.Lasso(alpha=0.5), "LassoRegression"),
    (linear_model.Ridge(alpha=0.5), "RidgeRegression"),
    (linear_model.ElasticNet(alpha=0.5, l1_ratio=0.7), "ElasticNet")):
    print('=' * 80)
    print(name)

    output_file = sys.argv[3] + '/' + name + '5.csv'
    with open(output_file, 'w') as out:
        field_name = ["name", "class0", "TP0", "FP0", "FN0", "Precision0", "Recall0", "class1", "TP1", "FP1", "FN1",
                      "Precision1", "Recall1"]
        writer = csv.DictWriter(out, fieldnames=field_name)
        writer.writeheader()
        output_dict = dict()

        train_file = ''
        test_file = ''
        for trainfile in train_file_list:
            train = os.path.basename(trainfile).split('.')[0].split('_')[1]

            for testfile in test_file_list:
                test = os.path.basename(testfile).split('.')[0]
                if train == test:
                    train_file = trainfile
                    test_file = testfile
                    rt = RegressionBase(train_file, test_file)
                    X_train, y_train, X_test, y_test = rt.Test()
                    print train_file, test_file

                    pred, act, num0, num1 = benchmark(clf, name, X_train, y_train, X_test, y_test)

                    p, r, f, s = precision_recall_fscore_support(y_true=np.array(act), y_pred=np.array(pred), average=None,
                                                     sample_weight=None, labels=labels)
                    tp, fp, fn = RegressionBase.tp_fp_fn(pre_y=np.array(pred), act_y=np.array(act))


                    output_dict['name'] = train
                    output_dict["class0"] = num0
                    output_dict["TP0"] = tp[0]
                    output_dict["FP0"] = fp[0]
                    output_dict["FN0"] = fn[0]
                    output_dict["Precision0"] = "{0:0.{1}f}".format(p[1], 2)
                    output_dict["Recall0"] = "{0:0.{1}f}".format(r[1], 2)
                    output_dict["class1"] = num1
                    output_dict["TP1"] = tp[1]
                    output_dict["FP1"] = fp[1]
                    output_dict["FN1"] = fn[1]
                    output_dict["Precision1"] = "{0:0.{1}f}".format(p[0], 2)
                    output_dict["Recall1"] = "{0:0.{1}f}".format(r[0], 2)
                    writer.writerow(output_dict)
                    output_dict.clear()