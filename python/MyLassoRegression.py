from sklearn import linear_model
from RegressionBase import *
import sys,csv

def Core(train_x, train_y, test_x, test_y):
    #rr = linear_model.Ridge(alpha=0.5)
    rr = linear_model.Lasso(alpha=0.5)
    rr.fit(train_x, train_y)
    output_file = sys.argv[3]


    s = rr.get_params()
    print s
    Y_rr_pre = rr.predict(test_x)
    #Y_rr_pre = cross_val_predict(rr, train_x, train_y, cv=10)
    print np.mean((Y_rr_pre - test_y) ** 2)
    print rr.score(test_x, test_y)
    print rr.intercept_
    print rr.coef_

    precision0 = []
    precision1 = []
    recall0 = []
    recall1 = []
    labels = [1, 0]
    target_names = ['class 1', 'class 0']
    with open(output_file, 'w') as out:
        field_name = ["class0", "TP0", "FP0", "FN0", "class1", "TP1", "FP1", "FN1"]
        writer = csv.DictWriter(out, fieldnames=field_name)
        writer.writeheader()
        output_dict = dict()

        for x in [x / 10.0 for x in range(10, 51, 1)]:
            Y_pre, _, _  = RegressionBase.Timeout(Y_rr_pre, x)
            Y_act, num0, num1 = RegressionBase.Timeout(test_y, x)

            #print Y_rr_pre, test_y

            p, r, f, s = precision_recall_fscore_support(y_true=np.array(Y_act), y_pred=np.array(Y_pre), average=None,
                                                         sample_weight=None, labels=labels)

            precision1.append("{0:0.{1}f}".format(p[0], 2))
            precision0.append("{0:0.{1}f}".format(p[1], 2))

            recall1.append("{0:0.{1}f}".format(r[0], 2))
            recall0.append("{0:0.{1}f}".format(r[1], 2))

            print classification_report(y_pred=np.array(Y_pre), y_true=np.array(Y_act), labels=labels,
                                        target_names=target_names)
            tp, fp, fn = RegressionBase.tp_fp_fn(pre_y=np.array(Y_pre), act_y=np.array(Y_act))
            string1 = "Class 0 :%(num0)d TP:%(tp)d\tFP:%(fp)d\tFN:%(fn)d\n" % {'num0':num0,'tp': tp[0], 'fp':fp[0], 'fn':fn[0]}
            string2 = "Class 1 :%(num1)d TP:%(tp)d\tFP:%(fp)d\tFN:%(fn)d\n" % {'num1':num1,'tp': tp[1], 'fp': fp[1], 'fn': fn[1]}
            #print "Class 0 TP:%(tp)d\tFP:%(fp)d\tFN:%(fn)d\n" % {'tp': tp[0], 'fp':fp[0], 'fn':fn[0]}
            #print "Class 1 TP:%(tp)d\tFP:%(fp)d\tFN:%(fn)d\n" % {'tp': tp[1], 'fp': fp[1], 'fn': fn[1]}

            output_dict["class0"] = num0
            output_dict["TP0"] = tp[0]
            output_dict["FP0"] = fp[0]
            output_dict["FN0"] = fn[0]
            output_dict["class1"] = num1
            output_dict["TP1"] = tp[1]
            output_dict["FP1"] = fp[1]
            output_dict["FN1"] = fn[1]
            writer.writerow(output_dict)
            print string1
            print string2
    RegressionBase.PlotPRCurve(timeout=[x / 10.0 for x in range(10, 51, 1)], actual_y= test_y, predict_y= Y_rr_pre, class0precision=precision0, class1precision=precision1, class0recall=recall0, class1recall=recall1)



trainx = []
trainy = []
testx = []
testy = []

rt = RegressionBase(sys.argv[1], sys.argv[2])
trainx, trainy, testx, testy = rt.Test()

Core(train_x=trainx, train_y=trainy, test_x=testx, test_y=testy)