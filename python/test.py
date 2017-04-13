from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support

y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
target_names = ['class 0', 'class 1', 'class 2']
labels = [0, 1, 2]
print(classification_report(y_true, y_pred, target_names=target_names, labels=labels))


p, r, f, s = precision_recall_fscore_support(y_true, y_pred)

width = 4
headers = ["precision", "recall", "f1-score", "support"]
fmt = '%% %ds' % width  # first column: class name
fmt += '  '
fmt += ' '.join(['% 9s' for _ in headers])
fmt += '\n'

headers = [""] + headers
report = fmt % tuple(headers)
report += '\n'

for i, label in enumerate(labels):
    values = [target_names[i]]
    for v in (p[i], r[i], f[i]):
        values += ["{0:0.{1}f}".format(v, 2)]
    values += ["{0}".format(s[i])]
    report += fmt % tuple(values)

print report