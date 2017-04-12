from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np



def LoadData(data_path):
    all_data = np.loadtxt(data_path, delimiter=',')
    print all_data

LoadData("/home/chaowyc/Documents/constraints/test/smt_attrs.csv")
