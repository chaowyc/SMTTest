import numpy as np
import sys
import os


def Timeout(data, threshold):
    return_value = []
    for x in data:
        if x <= threshold:
            return_value.append(1)
        else:

            return_value.append(0)
    return return_value

data_path = sys.argv[1]

all_data = np.loadtxt(data_path, delimiter=',')
row, col = all_data.shape
X = np.array(all_data[:, : col - 4])
push_Y = np.array(Timeout(all_data[:, -1], 1))
no_push_Y = np.array(Timeout(all_data[:, 33], 1))


push_output_filename = data_path + ".svm.push.1s"
with open(push_output_filename, "w") as out:
    output = ""
    for i in range(0, row):
        output += str(push_Y[i])
        for j in range(0, col - 4):
            output += " " + str(j + 1) + ':' + str(X[i, j])
        output += "\n"
        print "\r%(num1)d/%(num2)d.." % {'num1': i + 1, 'num2':row} ,
        out.write(output)
        output = ''

no_push_output_filename = data_path + ".svm.nopush.1s"
print "\n"
with open(no_push_output_filename, "w") as outt:
    outputt = ""
    for i in range(0, row):
        outputt += str(no_push_Y[i])
        for j in range(0, col - 4):
            output += " " + str(j + 1) + ':' + str(X[i, j])
        outputt += "\n"
        print "\r%(num1)d/%(num2)d.." % {'num1': i + 1, 'num2':row} ,
        outt.write(outputt)
        outputt = ''