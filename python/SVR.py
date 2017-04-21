from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
import numpy as np
from sklearn.svm.classes import SVR
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_pdf import PdfPages

def timeout(data, th):
    reval = []
    for x in data:
        if x <= th:
            reval.append(1)
        else:
            reval.append(0)
    return reval

def PlotPR(x, y0, y1, z0, z1):
    f, axarr = plt.subplots(2, sharex=True)

    pp = PdfPages('PR.pdf')
    axarr[0].set_title('Timeout Class(Class 0) Precision/Recall')
    axarr[0].plot(x, y0, label="Precision")
    for i, j in zip(x, y0):
        axarr[0].annotate(str(j), xy=(i, j))

    axarr[0].plot(x, z0, label='Recall')
    for i, j in zip(x, z0):
        axarr[0].annotate(str(j), xy=(i, j))

    axarr[1].set_title('Non-Timeout Class(Class 1)Precision/Recall')
    axarr[1].plot(x, y1, label="Precision")
    for i, j in zip(x, y1):
        axarr[1].annotate(str(j), xy=(i, j))
    axarr[1].plot(x, z1, label="Recall")
    for i, j in zip(x, z1):
        axarr[1].annotate(str(j), xy=(i, j))

    plt.legend(bbox_to_anchor=(0.75, 0.3), loc=2, mode="expand", borderaxespad=0.)
    plt.show()
    f.savefig(pp, format='pdf')
    f.savefig("PR.png")
    pp.close()

all_data = np.loadtxt(sys.argv[1], delimiter=',')
row, col = all_data.shape
X = all_data[:, : col - 4]
#Y = all_data[:, col - 3]
Y = all_data[:, -1]

print Y

pre = []
act = []

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#print Y_test

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1, verbose=True)

svr_rbf.fit(X_train, Y_train)
#print svr_rbf
Y_rbf = svr_rbf.predict(X_test)

precision0 = []
precision1 = []
recall0 = []
recall1 = []

labels = [1, 0]
target_names = ['class 1', 'class 0']
precision_recall_dict = dict()

for x in [x / 10.0 for x in range(10, 51, 1)]:
    Y_pre = timeout(Y_rbf, x)
    Y_act = timeout(Y_test, x)

    p, r, f, s = precision_recall_fscore_support(y_true=np.array(Y_act), y_pred=np.array(Y_pre), average=None, sample_weight=None, labels=labels)

    precision1.append("{0:0.{1}f}".format(p[0], 2))
    precision0.append("{0:0.{1}f}".format(p[1], 2))

    recall1.append("{0:0.{1}f}".format(r[0], 2))
    recall0.append("{0:0.{1}f}".format(r[1], 2))

    print classification_report(y_pred=np.array(Y_pre), y_true=np.array(Y_act), labels=labels, target_names=target_names)

PlotPR([x / 10.0 for x in range(10, 51, 1)], precision0, precision1, recall0, recall1)


#for i in range(0, len(Y_pre)):
#    print "%(num1)f\t%(num2)f" %{'num1' : Y_rbf[i], 'num2': Y_test[i]}











>>>>>>> 6164d8b30ffb09619fb4e1b123d47c24b948e6a8




