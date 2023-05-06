import random
import json

persons = []
groups = []
messages = []

with open('./settings.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)
    op_type = data["op_type"]

    lines = data["lines"]
    people_num = data["people_num"]
    group_num = data["group_num"]
    messages_num = data["messages_num"]
    print(data)


class people:
    def __init__(self, id):
        self.id = id
        self.acq = []

    def isRela(self, id):
        for person in self.acq:
            if id == person:
                return True
        return False


class TestPeople:
    def __init__(self, id):
        self.id = id
        self.acq = {}


class group:
    def __init__(self, id):
        self.id = id
        self.people = []

    def containPerson(self, id):
        for person in self.people:
            if id == person:
                return True
        return False


def printAllPersons(persons):
    line = str(len(persons)) + " "
    for person in persons:
        line = line + str(person.id) + " "
    for person in persons:
        line = line + str(len(person.acq)) + " "
        for id in person.acq:
            line = line + str(id) + " 1 "
    print("qtsok " + line + line)


def containPeople(id):
    for person in persons:
        if person.id == id:
            return True
    return False


def containGroup(id):
    for group in groups:
        if group.id == id:
            return True
    return False


def containMessage(id):
    for message in messages:
        if message == id:
            return True
    return False


def getGroup(id):
    for group in groups:
        if group.id == id:
            return group
    return None


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


def add_group():
    id = random.randint(-group_num / 2, group_num)
    if len(groups) == 0:
        groups.append(group(id))
    elif not containGroup(id):
        groups.append(group(id))
    return "ag " + str(id)


def add_to_group():
    flag = rd(0, 4)
    if flag == 0 or len(persons) == 0 or len(groups) == 0:
        id1 = rd(-group_num / 2, group_num)
        id2 = rd(-people_num / 2, people_num / 2)
    else:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = groups[rd(0, len(groups) - 1)].id
    if containPeople(id1) and containGroup(id2) and getGroup(id2).containPerson(id1) == False:
        getGroup(id2).people.append(id1)
    return "atg " + str(id1) + " " + str(id2)


def del_from_group():
    flag = rd(0, 4)
    if flag == 0 or len(persons) == 0 or len(groups) == 0:
        id1 = rd(-group_num / 2, group_num)
        id2 = rd(-people_num / 2, people_num / 2)
    else:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = groups[rd(0, len(groups) - 1)].id
    if containPeople(id1) and containGroup(id2) and getGroup(id2).containPerson(id1):
        getGroup(id2).people.remove(id1)
    return "dfg " + str(id1) + " " + str(id2)


def query_group_value_sum():
    flag = rd(0, 1)
    if flag == 0 or len(groups) == 0:
        id = rd(-group_num / 2, group_num)
    else:
        id = groups[rd(0, len(groups) - 1)].id
    return "qgvs " + str(id)


def query_group_age_var():
    flag = rd(0, 1)
    if flag == 0 or len(groups) == 0:
        id = rd(-group_num / 2, group_num)
    else:
        id = groups[rd(0, len(groups) - 1)].id
    return "qgav " + str(id)


def modify_relation():
    flag = rd(0, 4)
    if flag == 0 or len(persons) == 0:
        id1 = rd(-people_num / 2, people_num / 2)
        id2 = rd(-people_num / 2, people_num / 2)
    else:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    value = rd(-100, 100)
    return "mr " + str(id1) + " " + str(id2) + " " + str(value)


def query_best_acquaintance():
    flag = rd(0, 1)
    if flag == 0 or len(persons) == 0:
        id = rd(-people_num / 2, people_num / 2)
    else:
        id = persons[rd(0, len(persons) - 1)].id
    return "qba " + str(id)


def query_couple_sum():
    return "qcs"


def add_message():
    id = rd(-messages_num / 2, messages_num / 2)
    type = rd(0, 1)
    flag = rd(0, 2)
    if flag == 0 or len(persons) == 0:
        id1 = rd(-people_num / 2, people_num / 2)
    else:
        id1 = persons[rd(0, len(persons) - 1)].id
    socialValue = rd(-1000, 1000)
    if type == 0:
        flag = rd(0, 2)
        if flag == 0 or len(persons) == 0:
            id2 = rd(-people_num / 2, people_num / 2)
        else:
            id2 = persons[rd(0, len(persons) - 1)].id
    else:
        flag = rd(0, 2)
        if flag == 0 or len(groups) == 0:
            id2 = rd(-group_num / 2, group_num / 2)
        else:
            id2 = groups[rd(0, len(groups) - 1)].id
    if containPeople(id1) and (
            (type == 0 and containPeople(id2) and id1 != id2) or (type == 1 and containGroup(id2))) and containMessage(
            id) == False:
        messages.append(id)
    return "am " + str(id) + " " + str(socialValue) + " " + str(type) + " " + str(id1) + " " + str(id2)


def send_message():
    flag = rd(0, 2)
    if flag == 0 or len(messages) == 0:
        id = rd(-messages_num / 2, messages_num / 2)
    else:
        id = messages[rd(0, len(messages) - 1)]
    return "sm " + str(id)


def query_social_value():
    flag = rd(0, 1)
    if flag == 0 or len(persons) == 0:
        id = rd(-people_num / 2, people_num / 2)
    else:
        id = persons[rd(0, len(persons) - 1)].id
    return "qsv " + str(id)


def query_received_messages():
    flag = rd(0, 1)
    if flag == 0 or len(persons) == 0:
        id = rd(-people_num / 2, people_num / 2)
    else:
        id = persons[rd(0, len(persons) - 1)].id
    return "qrm " + str(id)


def add_person():
    id = random.randint(-people_num / 2, people_num / 2)
    name = "1"
    age = rd(0, 200)
    if len(persons) == 0:
        persons.append(people(id))
    elif not containPeople(id):
        persons.append(people(id))
    return "ap " + str(id) + " " + name + " " + str(age)


def add_relation():
    flag = rd(0, 5)
    if len(persons) > 2 and flag != 5:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    else:
        id1 = random.randint(-people_num / 2, people_num / 2)
        id2 = random.randint(-people_num / 2, people_num / 2)
    if containPeople(id1) and containPeople(id2) and id1 != id2:
        addRelation(id1, id2)
    value = rd(1, 100)
    return "ar " + str(id1) + " " + str(id2) + " " + str(value)


def query_value():
    flag = rd(0, 5)
    if len(persons) > 2 and flag != 5:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    else:
        id1 = random.randint(-people_num / 2, people_num / 2)
        id2 = random.randint(-people_num / 2, people_num / 2)
    return "qv " + str(id1) + " " + str(id2)


def query_circle():
    flag = rd(0, 5)
    if len(persons) > 2 and flag != 5:
        id1 = persons[rd(0, len(persons) - 1)].id
        id2 = persons[rd(0, len(persons) - 1)].id
    else:
        id1 = random.randint(-people_num / 2, people_num / 2)
        id2 = random.randint(-people_num / 2, people_num / 2)
    return "qci " + str(id1) + " " + str(id2)


def query_block_sum():
    return "qbs"


def query_triple_sum():
    return "qts"


def gen_person_line(inputs) -> str:
    in_line = str(len(inputs)) + " "
    for pid, person in inputs.items():
        in_line = in_line + str(pid) + " "
    for pid, person in inputs.items():
        in_line = in_line + str(len(person.acq)) + " "
        for sub_pid, value in person.acq.items():
            in_line = in_line + str(sub_pid) + " {:d} ".format(value)
    return in_line


def generate_data_small() -> []:
    pool = {ii: TestPeople(ii) for ii in range(-5, 5)}
    # print(pool)
    relations = []
    for ii in range(-5, 5):
        for jj in range(ii + 1, 5):
            quotient = rd(0, 2)
            if quotient == 1:
                relations.append([ii, jj])
    if len(relations) == 0:
        relations.append([-1, 1])
    for relation in relations:
        value = rd(1, 100)
        pool[relation[0]].acq[relation[1]] = value
        pool[relation[1]].acq[relation[0]] = value
    return pool


bound = 5
value_bound = 100


def remove_dup(pool, who):
    for pid, person in pool.items():
        if who in pool[pid].acq:
            pool[pid].acq.pop(who)


def modify_relation_test() -> str:
    pool = generate_data_small()
    inputs = []
    has_acq = []
    for pid, person in pool.items():
        inputs.append(person)
        if len(person.acq) != 0:
            has_acq.append(pid)
    # print(inputs)
    mode = random.randint(0, 16)
    # mode = 9
    before = ""
    after = ""
    entry_req = ""
    params = [-1, -2, 50]
    if mode == 0:  # judge exception
        quotient = rd(0, 4)
        if quotient == 0:
            params[0] = (-0x7f7f7f7f)
            params[1] = (-0x7f7f7f80)
            params[2] = 20
            before = gen_person_line(pool)
            after = before
        elif quotient == 1:
            params[0] = 0
            params[1] = 0
            params[2] = 20
            before = gen_person_line(pool)
            after = before
        elif quotient == 2:
            who = has_acq[rd(0, len(has_acq) - 1)]
            for pid, value in pool[who].acq.items():
                params[0] = who
                params[1] = pid
                params[2] = rd(-100, 100)
                pool[who].acq.pop(pid)
                pool[pid].acq.pop(who)
                break
            before = gen_person_line(pool)
            after = before
        elif quotient == 3:
            who = has_acq[rd(0, len(has_acq) - 1)]
            for pid, value in pool[who].acq.items():
                params[0] = who
                params[1] = pid
                params[2] = rd(-100, 100)
                pool[who].acq[pid] = pool[who].acq[pid] // 2
                break
            before = gen_person_line(pool)
            after = before
    elif mode == 1:  # 1
        params[0] = rd(-bound, bound)
        params[1] = rd(-bound, bound)
        while params[0] == params[1]:
            params[1] = rd(-bound, bound)
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq)) - 1]
        for pid, value in pool[who].acq.items():
            pool[pid].acq.pop(who)
        pool.pop(who)
        remove_dup(pool, who)
        after = gen_person_line(pool)
    elif mode == 2:  # 3
        params[0] = rd(-bound, bound)
        params[1] = rd(-bound, bound)
        while params[0] == params[1]:
            params[1] = rd(-bound, bound)
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            pool[pid].acq.pop(who)
        pool.pop(who)
        remove_dup(pool, who)
        pool[bound + 1] = TestPeople(bound + 1)
        after = gen_person_line(pool)
    elif mode == 3:  # 3
        params[0] = rd(-bound, bound)
        params[1] = rd(-bound, bound)
        while params[0] == params[1]:
            params[1] = rd(-bound, bound)
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            pool[pid].acq.pop(who)
            pool[who].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 4:  # 4, 15
        before = gen_person_line(pool)
        quotient = rd(0, 2)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        if quotient == 0:
            params[2] = -params[2] - 1
        else:
            params[2] = -params[2] + 1
            pool[params[0]].acq.pop(params[1])
            pool[params[1]].acq.pop(params[0])
        after = gen_person_line(pool)
    elif mode == 5:  # 5
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1
        after = gen_person_line(pool)
    elif mode == 6:  # 6
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[0]].acq[params[1]] = 1
        after = gen_person_line(pool)
    elif mode == 7:  # 7
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[1]].acq[params[0]] = 1
        pool[params[0]].acq[params[1]] = 1
        for pid, value in pool[params[0]].acq.items():
            if pid == params[1]:
                continue
            pool[params[0]].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 8:  # 8
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[1]].acq[params[0]] = 1
        pool[params[0]].acq[params[1]] = 1
        for pid, value in pool[params[1]].acq.items():
            if pid == params[0]:
                continue
            pool[params[1]].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 9:  # 9
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[1]].acq[params[0]] = 1
        pool[params[0]].acq[params[1]] = 1
        for pid, value in pool[params[0]].acq.items():
            if pid == params[1]:
                continue
            for pid1 in range(-bound, bound):
                if pid1 == params[0]:
                    continue
                if pid1 not in pool[params[0]].acq:
                    pool[params[0]].acq[pid1] = rd(0, value_bound)
                    break
            pool[params[0]].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 10:  # 10
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[1]].acq[params[0]] = 1
        pool[params[0]].acq[params[1]] = 1
        for pid, value in pool[params[1]].acq.items():
            if pid == params[0]:
                continue

            # pool[bound + 1] = TestPeople(bound + 1)
            for pid1 in range(-bound, bound):
                if pid1 == params[1]:
                    continue
                if pid1 not in pool[params[1]].acq:
                    pool[params[1]].acq[pid1] = rd(0, value_bound)
                    break
            pool[params[1]].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 11:  # 11
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[1]].acq[params[0]] = 1
        pool[params[0]].acq[params[1]] = 1
        for pid, value in pool[params[0]].acq.items():
            if pid == params[1]:
                continue
            pool[params[0]].acq[pid] = pool[params[0]].acq[pid] // 2
            break
        after = gen_person_line(pool)
    elif mode == 12:  # 12
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] + 1  # do not modify
        pool[params[1]].acq[params[0]] = 1
        pool[params[0]].acq[params[1]] = 1
        for pid, value in pool[params[1]].acq.items():
            if pid == params[0]:
                continue
            pool[params[1]].acq[pid] = pool[params[1]].acq[pid] // 2
            break
        after = gen_person_line(pool)
    elif mode == 13:  # 18
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] - 1  # do not modify
        pool[params[1]].acq.pop(params[0])
        pool[params[0]].acq.pop(params[1])
        for pid, value in pool[params[0]].acq.items():
            pool[params[0]].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 14:  # 19
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] - 1  # do not modify
        pool[params[1]].acq.pop(params[0])
        pool[params[0]].acq.pop(params[1])
        for pid, value in pool[params[1]].acq.items():
            pool[params[1]].acq.pop(pid)
            break
        after = gen_person_line(pool)
    elif mode == 15:  # 20
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] - 1  # do not modify
        pool[params[1]].acq.pop(params[0])
        pool[params[0]].acq.pop(params[1])
        for pid, value in pool[params[0]].acq.items():
            quotient = rd(0, 2)
            if quotient == 0:
                pool[params[0]].acq.pop(pid)
                pool[params[0]].acq[bound + 1] = rd(0, value_bound)
            else:
                pool[params[0]].acq[pid] = pool[params[0]].acq[pid] // 2
            break
        after = gen_person_line(pool)
    elif mode == 16:  # 21
        before = gen_person_line(pool)
        who = has_acq[rd(0, len(has_acq) - 1)]
        for pid, value in pool[who].acq.items():
            params[0] = who
            params[1] = pid
            params[2] = pool[pid].acq[who]
            break
        params[2] = -params[2] - 1  # do not modify
        pool[params[1]].acq.pop(params[0])
        pool[params[0]].acq.pop(params[1])
        for pid, value in pool[params[1]].acq.items():
            quotient = rd(0, 2)
            if quotient == 0:
                pool[params[1]].acq.pop(pid)
                pool[params[1]].acq[bound + 1] = rd(0, value_bound)
            else:
                pool[params[1]].acq[pid] = pool[params[1]].acq[pid] // 2
            break
        after = gen_person_line(pool)
    else:
        before = gen_person_line(pool)
        after = before
    entry_req = before + "{} {} {} ".format(params[0], params[1], params[2]) + after
    return entry_req


print_qtsok = False


def generate_data():
    persons.clear()
    groups.clear()
    messages.clear()  # clear element
    data1 = ""
    ge = ""
    for i in range(lines):
        if op_type == 0:
            flag = rd(0, 32)
            if flag < 6:
                ge = add_person()
            elif flag >= 6 and flag < 12:
                ge = add_relation()
            elif flag == 12:
                ge = query_value()
            elif flag == 13:
                ge = query_circle()
            elif flag == 14:
                ge = query_block_sum()
            elif flag == 15:
                ge = query_triple_sum()
            elif flag >= 16 and flag <= 17:
                ge = add_group()
            elif flag >= 18 and flag <= 20:
                ge = add_to_group()
            elif flag == 21:
                ge = del_from_group()
            elif flag == 22:
                ge = query_group_value_sum()
            elif flag == 23:
                ge = query_group_age_var()
            elif flag == 24 or flag == 25:
                ge = modify_relation()
            elif flag == 26:
                ge = query_best_acquaintance()
            elif flag >= 27 and flag <= 28:
                ge = add_message()
            elif flag >= 29 and flag <= 30:
                ge = send_message()
            elif flag == 31:
                ge = query_social_value()
            elif flag == 32:
                ge = query_couple_sum()
        if op_type == 1:
            ge = "mrok " + modify_relation_test()
        data1 = data1 + ge + "\n"
    return data1
