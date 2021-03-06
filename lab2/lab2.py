meaning = {0 : "lion", 1 : "fox", 2 : "goose", 3 : "corn"}

goal = [True, True, True, True]
bank = [False, False, False, False]     # start position

var = [[1,3], [2,3], [0], [1], [2], [3]]    # possible movements in boat
ok = [[0,3], [1,2], [1,3]]

result = [bank]

flag = True

def not_forbiden_chek(b, here):
    if not b in result:
        flag = not here
        if b[0] == flag and b[1] == flag:
            print("\n-lion and fox can`t be both on one side")
            return False
        elif b[1] == flag and b[2] == flag:
            print("\n-fox and goose can`t be both on one side")
            return False
        elif b[2] == flag and b[3] == flag:
            print("\n-goose and corn can`t be both on one side")
            return False
        else:
            return True
    else:
        return False


def move(c, i, at):
    new_s = c.copy()
    if at:
        direction = " from 1 to 2"
    else:
        direction = " from 2 to 1"
    if len(i) == 1 :
        new_s[i[0]] = not new_s[i[0]]
        # iteration 2->1 fox : value change by itself result[1] to false
    else:
        if new_s[i[0]] == new_s[i[1]]:
            new_s[i[0]] = not new_s[i[0]]
            new_s[i[1]] = not new_s[i[1]]
    if not_forbiden_chek(new_s, at):
        if len(i) == 1 :
            print("\n! relocating ", meaning[i[0]], direction)
        else:
            print("\n! relocating ", meaning[i[0]], " and ", meaning[i[1]], direction)
        result.append(new_s)
        return new_s
    else:
        # print("\noops - can`t move", i, direction)
        return c

def is_ok(c, pos):
    if not c in result[:-1]:
        b2 = []
        if pos:       
            i = 0
            while i <= 3:
                if c[i] == True :
                    b2.append(i)
                i += 1
        if b2 in ok: 
            return True
        else:
            return False
    else:
        return False

def successor(cur):
    if cur == goal:
        return True
    else:
        return False

def func(next_s, prev, pos):
    res = []
    if prev != next_s:   
        if successor(next_s):
            print("\n!!! success")
            res.append(True)
            res.append(True)
        else:
            res.append(False)
            res.append(True)
            if is_ok(next_s, pos):
                pos = not pos
                print("\n! going back emptyhanded")
            # continue
        res.append(pos)
        return res
    else:
        pos = not pos
        res.append(False)
        res.append(False)
        res.append(pos)
        return res


def RBFS(cur, pos):
    next_s = cur.copy()

    for v in var:
        pos = not pos
        prev = next_s.copy()
        next_s = move(next_s, v, pos)
        res = func(next_s, prev, pos)
        pos = res[2]
        if res[0] == True:
            break
        elif res[1] == True:
            RBFS(next_s, pos)
        else:
            continue
    print("check")
    print("check")


        


def driver():
    at_bank = False
    print("\nRBFS")
    cur_state = bank    # initialising
    RBFS(cur_state, at_bank)
    print("\nResult: ", result)

driver()

