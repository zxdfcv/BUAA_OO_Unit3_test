import os
import random
# from xeger import Xeger
import random
import shutil
import subprocess
import threading
from subprocess import STDOUT, PIPE
import sys

semaphore = threading.Semaphore(25)


class people:
    def __init__(self, pid):
        self.id = pid
        self.acq = []

    def isRela(self, pid):
        for person in self.acq:
            if pid == person:
                return True
        return False

main_jar = "longfei.jar"
jars = ["person1.jar", "person2.jar"]
global wrong
wrong = 0
persons = []
filepath = "./data.txt"


def execute_java(stdin, jar):
    semaphore.acquire()
    cmd = ['java', '-jar', jar]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate(stdin.encode())
    if len(stderr.decode().strip()) > 0:
        print("!!RE!! with " + str(jar).split(".")[0] + " input :")
        print(stdin)
        print(stderr.decode())
        semaphore.release()
        exit(1)
    semaphore.release()
    return stdout.decode().strip()


def printAllPersons(persons):
    line = str(len(persons)) + " "
    for person in persons:
        line = line + str(person.id) + " "
    for person in persons:
        line = line + str(len(person.acq)) + " "
        for id in person.acq:
            line = line + str(id) + " 1 "
    print("qtsok " + line + line)


def judge(filename, jar1, jar2, round):
    with open(filename) as f:
        data = f.read()
    f.close()
    lines = data.split("\n")
    ans1 = execute_java(data, jar1).replace("\r", "").split("\n")
    ans2 = execute_java(data, jar2).replace("\r", "").split("\n")
    if len(ans1) != len(ans2):
        print("{} len wrong! at file{}".format(str(jar1).split(".")[0], str(round)))
        with open("./" + str(jar1).split(".")[0] + "/" + str(round) + ".txt", 'w+') as file:
            file.truncate(0)
            file.write("len wrong!\n")
            file.write(data)
        return
    else:
        for i in range(len(ans1)):
            if ans1[i] != ans2[i]:
                print("{} wrong answer!\ndata: " + lines[i] + "\nyours: " + ans1[i] + "\nreference: " + ans2[i] +
                      "\nat line:{} at file{}".
                      format(str(jar1).split(".")[0], str(i + 1), str(round)))
                with open("./" + str(jar1).split(".")[0] + "/" + str(round) + ".txt", 'w+') as file:
                    file.truncate(0)
                    file.write("wrong answer at {}!\n".format(str(i)))
                    file.write(data)
                return
    print(str(jar1).split(".")[0] + " round" + str(round) + " ac")


def containPeople(id):
    for person in persons:
        if person.id == id:
            return True
    return False


def addRelation(id1, id2):
    people1 = None
    people2 = None
    for person in persons:
        if person.id == id1:
            people1 = person
        elif person.id == id2:
            people2 = person
    if not people1.isRela(id2):
        people1.acq.append(id2)
        people2.acq.append(id1)


def rd(a, b):
    return random.randint(a, b)


def add_person():
    id = random.randint(1, people_num)
    name = "1"
    age = "1"
    if len(persons) == 0:
        persons.append(people(id))
    elif not containPeople(id):
        persons.append(people(id))
    return "ap " + str(id) + " " + name + " " + age


def add_relation():
    flag = rd(0, 5)
    if len(persons) > 2 and flag != 5:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    else:
        id1 = random.randint(1, people_num)
        id2 = random.randint(1, people_num)
    if containPeople(id1) and containPeople(id2) and id1 != id2:
        addRelation(id1, id2)
    return "ar " + str(id1) + " " + str(id2) + " " + "1"


def query_value():
    flag = rd(0, 5)
    if len(persons) > 2 and flag != 5:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    else:
        id1 = random.randint(1, people_num)
        id2 = random.randint(1, people_num)
    return "qv " + str(id1) + " " + str(id2)


def query_circle():
    flag = rd(0, 5)
    if len(persons) > 2 and flag != 5:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    else:
        id1 = random.randint(1, people_num)
        id2 = random.randint(1, people_num)
    return "qci " + str(id1) + " " + str(id2)


def query_block_sum():
    return "qbs"


def query_triple_sum():
    return "qts"


num = 100
people_num = 40
lines = 100

print_qtsok = False


def generate_data() -> str:
    persons = []
    line = lines
    data = ""
    while line != 0:
        flag = rd(0, 18)
        if flag < 10:
            ge = add_person()
            data = data + ge + "\n"
        elif flag >= 10 and flag < 15:
            ge = add_relation()
            data = data + ge + "\n"
        elif flag == 15:
            ge = query_value()
            data = data + ge + "\n"
        elif flag == 16:
            ge = query_circle()
            data = data + ge + "\n"
        elif flag == 17:
            ge = query_block_sum()
            data = data + ge + "\n"
        elif flag == 18:
            ge = query_triple_sum()
            data = data + ge + "\n"
        line = line - 1
    with open(filepath, 'w+') as file:
        file.truncate(0)
        file.write(data)

    # print(query_triple_sum())
    # line = str(len(persons)) + " "
    # for person in persons :
    #     line = line + str(person.id) + " "
    # for person in persons :
    #     line = line + str(len(person.acq)) + " "
    #     for id in person.acq:
    #         line = line + str(id) + " 1 "
    # print("qtsok " + line + line)
    return data


def sub_judge(input_id, jar):
    # for ii in range(0, num, 5):
    #     for jj in range(ii, ii + 5):
    #         if jj >= num:
    #             break
    #         print(jj)
    filename = "./input/file{:d}.txt".format(input_id)
    semaphore.acquire()
    semaphore.release()
    threading.Thread(target=judge, args=(filename, jar, main_jar, input_id)).start()


for jar in jars:
    if os.path.exists(str(jar).split(".")[0]):
        shutil.rmtree(str(jar).split(".")[0])
    os.mkdir(str(jar).split(".")[0])

if os.path.exists("input"):
    shutil.rmtree("input")
os.mkdir("input")

for i in range(num):
    data = generate_data()
    filename = "./input/file{:d}.txt".format(i)
    with open(filename, "w") as f:
        f.write(data)
    f.close()

for ii in range(0, num):
    for jar in jars:
        sub_judge(ii, jar)

