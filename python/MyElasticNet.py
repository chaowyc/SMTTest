from sklearn import linear_model
from RegressionBase import *
import sys

def Core(train_x, train_y, test_x, test_y):
    #rr = linear_model.Ridge(alpha=0.5)
    rr = linear_model.ElasticNet(alpha=0.5, l1_ratio=0.7)
    rr.fit(train_x, train_y)
    Y_rr_pre = rr.predict(test_x)
    print rr.coef_
    print rr.alpha
    precision0 = []
    precision1 = []
    recall0 = []
    recall1 = []

    labels = [1, 0]
    target_names = ['class 1', 'class 0']

    for x in [x / 10.0 for x in range(10, 51, 1)]:
        Y_pre = RegressionBase.Timeout(Y_rr_pre, x)
        Y_act = RegressionBase.Timeout(test_y, x)

        #print Y_rr_pre, test_y

        p, r, f, s = precision_recall_fscore_support(y_true=np.array(Y_act), y_pred=np.array(Y_pre), average=None,
                                                     sample_weight=None, labels=labels)

        precision1.append("{0:0.{1}f}".format(p[0], 2))
        precision0.append("{0:0.{1}f}".format(p[1], 2))

        recall1.append("{0:0.{1}f}".format(r[0], 2))
        recall0.append("{0:0.{1}f}".format(r[1], 2))

        print classification_report(y_pred=np.array(Y_pre), y_true=np.array(Y_act), labels=labels,
                                    target_names=target_names)
    RegressionBase.PlotPRCurve([x / 10.0 for x in range(10, 51, 1)], precision0, precision1, recall0, recall1)



trainx = []
trainy = []
testx = []
testy = []

if len(sys.argv) == 2:
    rd = RegressionBase(sys.argv[1])
    trainx, trainy, testx, testy = rd.Demo()


elif len(sys.argv) == 3:
    rt = RegressionBase(sys.argv[1], sys.argv[2])
    trainx, trainy, testx, testy = rt.Test()

Core(train_x=trainx, train_y=trainy, test_x=testx, test_y=testy)