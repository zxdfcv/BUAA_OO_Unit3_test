import os
import shutil
import subprocess
import threading
from subprocess import STDOUT, PIPE

import generator

semaphore = threading.Semaphore(25)


class People:
    def __init__(self, pid):
        self.id = pid
        self.acq = []

    def is_rela(self, pid):
        for person in self.acq:
            if pid == person:
                return True
        return False


main_jar = "longfei.jar"
jars = ["oohomework_2023_21371055_hw_10.jar", "oohomework_2023_21371055_hw_10.jar"]
persons = []
filepath = "./data.txt"


def execute_java(stdin, jar1, round1):
    semaphore.acquire()
    cmd = ['java', '-jar', jar1]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate(stdin.encode())
    if len(stderr.decode().strip()) > 0:
        print("!!RE!! with " + str(jar).split(".")[0] + " input: {}".format(round1))
        with open("./" + str(jar1).split(".")[0] + "/" + str(round1) + ".txt", 'w+') as file:
            file.truncate(0)
            file.write("!!RE!! with " + str(jar).split(".")[0] + " input :\n")
            file.write(data)
        print(stdin)
        print(stderr.decode())
        semaphore.release()
        exit(1)
    semaphore.release()
    return stdout.decode().strip()


def judge(filename1, jar1, jar2, round1):
    with open(filename1) as ff:
        data1 = ff.read()
    ff.close()
    lines = data1.split("\n")
    ans1 = execute_java(data1, jar1, round1).replace("\r", "").split("\n")
    ans2 = execute_java(data1, jar2, round1).replace("\r", "").split("\n")
    if len(ans1) != len(ans2):
        print("{} len wrong! at file{}".format(str(jar1).split(".")[0], str(round1)))
        with open("./" + str(jar1).split(".")[0] + "/" + str(round1) + ".txt", 'w+') as file:
            file.truncate(0)
            file.write("len wrong!\n")
            file.write(data1)
        return
    else:
        for i in range(len(ans1)):
            if ans1[i] != ans2[i]:
                print("{} wrong answer!\ndata: " + lines[i] + "\nyours: " + ans1[i] + "\nreference: " + ans2[i] +
                      "\nat line:{} at file{}".
                      format(str(jar1).split(".")[0], str(i + 1), str(round1)))
                with open("./" + str(jar1).split(".")[0] + "/" + str(round1) + ".txt", 'w+') as file:
                    file.truncate(0)
                    file.write("wrong answer at {}!\n".format(str(i)))
                    file.write(data1)
                return
    print(str(jar1).split(".")[0] + " round" + str(round1) + " ac")


maxRound = 10000


# outer modules
def sub_judge(input_id, jar):
    filename1 = "./input/file{:d}.txt".format(input_id)
    semaphore.acquire()
    semaphore.release()
    threading.Thread(target=judge, args=(filename1, jar, main_jar, input_id)).start()


for jar in jars:
    if os.path.exists(str(jar).split(".")[0]):
        shutil.rmtree(str(jar).split(".")[0])
    os.mkdir(str(jar).split(".")[0])

if os.path.exists("input"):
    shutil.rmtree("input")
os.mkdir("input")  # remove

for i in range(maxRound):
    data = generator.generate_data()
    filename = "./input/file{:d}.txt".format(i)
    with open(filename, "w") as f:
        f.write(data)
    f.close()

for ii in range(0, maxRound):
    for jar in jars:
        sub_judge(ii, jar)
