import generator
import os
import shutil
import subprocess
from subprocess import STDOUT, PIPE

wrong_path = "./wrong/"
if os.path.exists("wrong"):
    shutil.rmtree("wrong")
os.mkdir("wrong")

global wrong
wrong = 0

def execute_java(stdin, jar):
    cmd = ['java', '-jar', jar]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate(stdin.encode())
    if len(stderr.decode().strip()) > 0:
        print("!!RE!! with " + "input :")
        print(stdin)
        print(stderr.decode())
        exit(1)
    return stdout.decode().strip()

def judge(data, jar1, jar2, round) :
    global wrong
    lines = data.split("\n")
    ans1 = execute_java(data, jar1).replace("\r", "").split("\n")
    ans2 = execute_java(data, jar2).replace("\r", "").split("\n")
    filepath = wrong_path + "wrong" + str(wrong) + ".txt"
    if len(ans1) != len(ans2) :
        print("len wrong")
        with open(filepath, 'a+') as file:
            file.truncate(0)
            file.write("len wrong")
            file.write("\n\n")
            file.write(data)
        wrong = wrong + 1
        return
    else:
        for i in range(len(ans1)):
            if ans1[i] != ans2[i]:
                wrong_line = "wrong!\ndata: " + lines[i] + "\nans1: " + ans1[i] + "\nans2: " + ans2[i] + " \nat {:d}".format(i)
                print(wrong_line)
                with open(filepath, 'a+') as file:
                    file.truncate(0)
                    file.write(wrong_line)
                    file.write("\n\n")
                    file.write(data)
                wrong = wrong + 1
                return
    print("round" + str(round) +" ac")



round = 100

for i in range(round) :
    data = generator.generate_data()
    judge(data, 'hw10.jar', 'yx.jar', i)