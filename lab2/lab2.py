meaning = {0 : "lion", 1 : "fox", 2 : "goose", 3 : "corn"}

goal = [True, True, True, True]
bank = [False, False, False, False]

var = [[0], [1], [2], [3], [2,3], [1,3]]    # possible movements in boat

result = []

def not_forbiden_chek(b, here):
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


def move(c, i, at):
    old = c.copy()
    if len(i) == 1 :
        c[i[0]] = not c[i[0]]
    else:
        if c[i[0]] == c[i[1]]:
            c[i[0]] = not c[i[0]]
            c[i[1]] = not c[i[1]]
    if not_forbiden_chek(c, at):
        if len(i) == 1 :
            print("\nRelocating ", meaning[i[0]])
        else:
            print("\nRelocating ", meaning[i[0]], " and ", meaning[i[1]])
        result.append(c)
        return c
    else:
        print("oops")
        return old


def RBFS(cur, pos):
    next_s = cur.copy()

    counter = 0
    while next_s != goal:
        for v in var:
            counter += 1
            pos = not pos
            prev = next_s.copy()
            next_s = move(next_s, v, pos)
            if prev == next_s:
                RBFS(next_s, pos)

    # # working secuence
    # pos = not pos
    # next_s = move(next_s, [1, 3], pos)
    # pos = not pos
    # pos = not pos
    # next_s = move(next_s, [0], pos)
    # pos = not pos
    # next_s = move(next_s, [1], pos)
    # pos = not pos
    # next_s = move(next_s, [2], pos)
    # pos = not pos
    # next_s = move(next_s, [3], pos)
    # pos = not pos
    # next_s = move(next_s, [1, 3], pos)

def driver():
    at_bank = False
    print("\nRBFS")
    cur_state = bank    # initialising
    RBFS(cur_state, at_bank)
    print("Result: ", result)

driver()

