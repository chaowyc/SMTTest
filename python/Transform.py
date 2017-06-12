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
output_path = sys.argv[2]

all_data = np.loadtxt(data_path, delimiter=',')
row, col = all_data.shape
X = np.array(all_data[:, : col - 2])
no_push_Y = np.array(Timeout(all_data[:, -1], 1))
#no_push_Y = np.array(Timeout(all_data[:, 33], 1))


#for x in [x / 10.0 for x in range(10, 51, 1)]:
#push_output_filename = data_path + ".svm.push." + str(x) + "s"
'''
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

'''

#no_push_output_filename = data_path + ".svm.nopush." + str(x) + "s"
no_push_output_filename = output_path + ".svm.1s"
print "\n"
with open(no_push_output_filename, "w") as outt:
    outputt = ""
    for ii in range(0, row):
        outputt += str(no_push_Y[ii])
        for jj in range(0, col - 2):
            outputt += " " + str(jj + 1) + ':' + str(X[ii, jj])
        outputt += "\n"
        print "\r%(num1)d/%(num2)d.." % {'num1': ii + 1, 'num2':row} ,
        outt.write(outputt)
        outputt = ''

print "class 0 : %(num1)d, class 1 : %(num2)d" %{'num1' : num0, 'num2' : num1}