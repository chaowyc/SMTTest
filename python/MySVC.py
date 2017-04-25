from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
import numpy as np
from sklearn.svm.classes import SVC
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_pdf import PdfPages


class MySVM():
    def __init__(self, train_data_path, test_data_path=None):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path

    def Timeout(self, data, threshold):
        return_value = []
        for x in data:
            if x <= threshold:
                return_value.append(1)
            else:

                return_value.append(0)
        return return_value

    def PlotPRCurve(self, x, y0, y1, z0, z1):
        figure, axarr = plt.subplots(2, sharex=True)
        pdf_output = PdfPages("SVR_PR.pdf")

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
        # plt.show()
        figure.savefig(pdf_output, format='pdf')
        figure.savefig("SVR_PR.png")
        pdf_output.close()

    def Demo(self):
        all_data = np.loadtxt(self.train_data_path, delimiter=',')
        row, col = all_data.shape
        X_s = all_data[:, : col - 4]
        Y_s = all_data[:, -1]

        for x in [x / 10.0 for x in range(10, 51, 1)]:
            Y = self.Timeout(Y_s, x)
            X_train, X_test, Y_train, Y_test = train_test_split(X_s, Y, test_size=0.2)
            self.Core(X_train, Y_train, X_test, Y_test)




    def Core(self, train_x, train_y, test_x, test_y):

        svr_rbf = SVC(C=1e3, gamma=0.1, verbose=True)
        svr_rbf.fit(train_x, train_y)
        Y_rbf_pre = svr_rbf.predict(test_x)

        precision0 = []
        precision1 = []
        recall0 = []
        recall1 = []

        labels = [1, 0]
        target_names = ['class 1', 'class 0']

        p, r, f, s = precision_recall_fscore_support(y_true=np.array(test_y), y_pred=np.array(Y_rbf_pre), average=None,
                                                     sample_weight=None, labels=labels)

        precision1.append("{0:0.{1}f}".format(p[0], 2))
        precision0.append("{0:0.{1}f}".format(p[1], 2))

        recall1.append("{0:0.{1}f}".format(r[0], 2))
        recall0.append("{0:0.{1}f}".format(r[1], 2))

        print classification_report(y_pred=np.array(Y_rbf_pre), y_true=np.array(test_y), labels=labels,
                                        target_names=target_names)
        #self.PlotPRCurve([x / 10.0 for x in range(10, 51, 1)], precision0, precision1, recall0, recall1)

if __name__ == "__main__":
    dd = MySVM(sys.argv[1])
    dd.Demo()