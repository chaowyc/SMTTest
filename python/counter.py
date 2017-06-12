import numpy as np
import sys
import os

num1 = 0
num0 = 0
def Timeout(data, threshold):
    return_value = []
    global num0
    global num1
    for x in data:
        if x <= threshold:
            return_value.append(1)

            num1 += 1
        else:

            num0 += 1
            return_value.append(0)
    return return_value

data_path = sys.argv[1]

all_data = np.loadtxt(data_path, delimiter=',')
row, col = all_data.shape
X = np.array(all_data[:, : col - 4])

push_Y = np.array(Timeout(all_data[:, -1], 1))
print "push class 0 : %(num1)d, class 1 : %(num2)d" %{'num1' : num0, 'num2' : num1}

num0 = 0
num1 = 0
no_push_Y = np.array(Timeout(all_data[:, 33], 1))
print "non-push class 0 : %(num1)d, class 1 : %(num2)d" %{'num1' : num0, 'num2' : num1}
