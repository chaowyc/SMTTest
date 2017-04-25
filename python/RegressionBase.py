from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
from sklearn import preprocessing
import numpy as np
from sklearn.svm.classes import SVR
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_pdf import PdfPages


class RegressionBase():

    def __init__(self, train_data_path, test_data_path = None):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path

    @staticmethod
    def Timeout(data, threshold):
        return_value = []
        for x in data:
            if x <= threshold:
                return_value.append(1)
            else:

                return_value.append(0)
        return return_value

    @staticmethod
    def PlotPRCurve(x, y0, y1, z0, z1):
        figure, axarr = plt.subplots(2, sharex=True)
        #pdf_output = PdfPages("SVR_PR.pdf")

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
        #figure.savefig(pdf_output, format='pdf')
        figure.savefig("SVR_PR.png")
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
        X = all_data[:, : col - 4]
        Y = all_data[:, -1]
        X, Y = self.Shuffle(X, Y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        return X_train, Y_train, X_test, Y_test

    def Test(self):
        train_data = np.loadtxt(self.train_data_path, delimiter=',')
        test_data = np.loadtxt(self.test_data_path, delimiter=',')

        train_row, train_col = train_data.shape
        test_row, test_col = test_data.shape

        print "train : test = %(num1)d : %(num2)d " % {'num1': (int(train_row) / int(test_row)), 'num2': 1}

        Train_X = preprocessing.scale(train_data[:, :train_row - 4])
        Train_Y = train_data[:, -1]
        Train_X, Train_Y = self.Shuffle(Train_X, Train_Y)
        Test_X = preprocessing.scale(test_data[:, :test_row - 4])
        Test_Y = test_data[:, -1]

        return Train_X, Train_Y, Test_X, Test_Y
