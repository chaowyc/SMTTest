from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
from sklearn import preprocessing
import numpy as np
from sklearn.svm.classes import SVR
import matplotlib.pyplot as plt
import sys, os
from matplotlib.backends.backend_pdf import PdfPages


class RegressionBase():

    def __init__(self, train_data_path, test_data_path = None):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.num1 = 0
        self.num0 = 0

    @staticmethod
    def Timeout(data, threshold):
        num1 = 0
        num0 = 0
        return_value = []
        for x in data:
            if x <= threshold:
                return_value.append(1)
                num1 += 1
            else:
                num0 += 1
                return_value.append(0)
        return return_value, num0, num1

    @staticmethod
    def PlotPRCurve(timeout, actual_y, predict_y, class0precision, class1precision, class0recall, class1recall):
        #pdf_output = PdfPages("SVR_PR.pdf")

        main_figure = plt.figure()
        ax1 = plt.subplot2grid((3, 9), (0, 0), colspan=6)
        ax2 = plt.subplot2grid((3, 9), (1, 0), colspan=6)
        ax3 = plt.subplot2grid((3, 9), (2, 0), colspan=6)
        ax4 = plt.subplot2grid((3, 9), (0, 6), colspan=3, rowspan=2)

        ax1.set_title("Regression")
        ax1.plot(actual_y, label="Actual")
        ax1.plot(predict_y, label="Predict")
        ax1.legend()

        ax2.set_title('Timeout Class(Class 0) Precision/Recall')
        ax2.plot(timeout, class0precision, label="Precision")
        ax2.plot(timeout, class0recall, label="Recall")
        ax2.legend()

        ax3.set_title('Non-Timeout Class(Class 1)Precision/Recall')
        ax3.plot(timeout, class1precision, label="Precision")
        ax3.plot(timeout, class1recall, label="Recall")
        ax3.legend()

        ax4.scatter(actual_y, predict_y)
        ax4.plot([actual_y.min(), actual_y.max()], [actual_y.min(), actual_y.max()], 'k--', lw=4)


        plt.tight_layout()



        #main_figure.savefig(pdf_output, format='pdf')
        main_figure.savefig("SVR_PR.png")
        #pdf_output.close()

    def LoadData(self):
        pass
    def Shuffle(self, trainx, trainy):
        permutation = np.random.permutation(trainy.shape[0])
        shuffled_dataset = trainx[permutation, :]
        shuffled_labels = trainy[permutation]
        return shuffled_dataset, shuffled_labels

    def Demo(self):
        all_data = np.loadtxt(self.train_data_path, delimiter=',')
        row, col = all_data.shape
        X = all_data[:, : col - 2]
        Y = all_data[:, -1]
        X, Y = self.Shuffle(X, Y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        return X_train, Y_train, X_test, Y_test

    def Test(self):
        print self.train_data_path, self.test_data_path

        train_data = np.loadtxt(self.train_data_path, delimiter=',')
        test_data = np.loadtxt(self.test_data_path, delimiter=',')

        train_row, train_col = train_data.shape
        test_row, test_col = test_data.shape

        print "train : test = %(num1)d : %(num2)d " % {'num1': (int(train_row) / int(test_row)), 'num2': 1}

        Train_X = preprocessing.scale(train_data[:, :train_row - 2])
        Train_Y = train_data[:, -1]
        Train_X, Train_Y = self.Shuffle(Train_X, Train_Y)
        Test_X = preprocessing.scale(test_data[:, :test_row - 2])
        Test_Y = test_data[:, -1]

        return Train_X, Train_Y, Test_X, Test_Y

    @staticmethod
    def tp_fp_fn(pre_y, act_y):
        tp = [0, 0]
        fp = [0, 0]
        fn = [0, 0]
        l = max(pre_y.shape)
        for i in range(0, l):
            if pre_y[i] == act_y[i]:
                if int(pre_y[i]) == 1:
                    tp[1] += 1
                else:
                    tp[0] += 1
            else:
                if int(pre_y[i]) == 1:
                    fp[1] += 1
                    fn[0] += 1
                elif int(pre_y[i]) == 0:
                    fn[1] += 1
                    fp[0] += 1

        return tp, fp, fn




