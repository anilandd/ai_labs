meaning = {0 : "lion", 1 : "fox", 2 : "goose", 3 : "corn"}

at_bank =  False
goal = [True, True, True, True]
bank = [False, False, False, False]

result = []


def not_forbiden_chek(b, present):
    if not present :
        if b[0] == True and b[1] == True:
            print("lion and fox can`t be both on one side")
            return False
        elif b[1] == True and b[2] == True:
            print("fox and goose can`t be both on one side")
            return False
        elif b[2] == True and b[3] == True:
            print("goose and corn can`t be both on one side")
            return False
        # not forbiden
        else:
            return True
    else:
        return True

# option 1 - boat: lion / fox / goose / corn
def trans_1(c, i):
    old = c.copy()
    c[i] = not c[i]
    at_bank = True
    if not_forbiden_chek(c, at_bank):
        print("\nRelocating ", meaning[i])
        print("next state is", c)
        result.append(c)
        return c
    else:
        print("oops")
        return old

# option 2 - boat: goose and corn / fox and corn
def trans_2(c, i, j):
    # check if at the same bank
    old = c.copy()
    if c[i] == c[j]:
        c[i] = not c[i]
        c[j] = not c[j]
        at_bank = True
        if not_forbiden_chek(c, at_bank):
            print("\nRelocating ", meaning[i], " and ", meaning[j])
            print("next state is", c)
            result.append(c)
            return c
        else:
            print("oops")
            return old

def RBFS(cur):
    next_s = cur.copy()

    next_s = trans_2(next_s, 1, 3)
    # return back
    next_s = trans_1(next_s, 0)
    next_s = trans_1(next_s, 1)
    next_s = trans_1(next_s, 2)
    next_s = trans_1(next_s, 3)
    next_s = trans_2(next_s, 1, 3)


def driver():
    print("RBFS")
    cur_state = bank    # initialising
    RBFS(cur_state)
    print("Result: ", result)


driver()
