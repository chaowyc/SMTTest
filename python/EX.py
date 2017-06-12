import subprocess

process = []

for i in range(1, 9):
    process.append(subprocess.Popen("./EX /dataset/case2/grep_cuted/0" + str(i) +"/ /dataset/result2/grep/", shell=True))


for p in process:
    p.wait()
