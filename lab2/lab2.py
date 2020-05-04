meaning = {0 : "lion", 1 : "fox", 2 : "goose", 3 : "corn"}

goal = [True, True, True, True]
bank = [False, False, False, False]     # start position

var = [[1,3], [2,3], [0], [1], [2], [3]]    # possible movements in boat
ok = [[0,3], [1,2], [1,3]]

result = [bank]

def not_forbiden_chek(b, here):
    if not b in result:
        flag = not here
        if b[0] == flag and b[1] == flag:
            print("! lion and fox can`t be both on one side")
            return False
        elif b[1] == flag and b[2] == flag:
            print("! fox and goose can`t be both on one side")
            return False
        elif b[2] == flag and b[3] == flag:
            print("! goose and corn can`t be both on one side")
            return False
        else:
            return True
    else:
        return False


def move(c, i, at):
    new_c = c.copy()
    if at:
        direction = " from 1 to 2"
    else:
        direction = " from 2 to 1"
    if len(i) == 1 :
        new_c[i[0]] = not new_c[i[0]]
    else:
        if new_c[i[0]] == new_c[i[1]]:
            new_c[i[0]] = not new_c[i[0]]
            new_c[i[1]] = not new_c[i[1]]
    if not_forbiden_chek(new_c, at):
        if len(i) == 1 :
            print("\nRelocating ", meaning[i[0]], direction, "\n")
        else:
            print("\nRelocating ", meaning[i[0]], " and ", meaning[i[1]], direction, "\n")
        result.append(new_c)
        return new_c
    else:
        print("oops - can`t move", i, direction)
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




def RBFS(cur, pos):
    next_s = cur.copy()
    counter = 0
    for v in var:
        counter += 1
        pos = not pos
        prev = next_s.copy()
        next_s = move(next_s, v, pos)
        if next_s == goal:
            break
        else:
            if prev != next_s:
                if is_ok(next_s, pos):
                    pos = not pos
                    print("Going back emptyhanded")
                    continue          
            else:
                pos = not pos
    print("\nResult:\n", result)
    print("\nEveryone on the second bank!")

def driver():
    at_bank = False
    print("\nRBFS")
    cur_state = bank    # initialising
    RBFS(cur_state, at_bank)

driver()

