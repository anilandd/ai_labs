meaning = {0 : "lion", 1 : "fox", 2 : "goose", 3 : "corn"}

goal = [True, True, True, True]
bank = [False, False, False, False]

result = []

def not_forbiden_chek(b, present):
    flag = not present
    # if not present :
    if b[0] == flag and b[1] == flag:
        print("lion and fox can`t be both on one side")
        return False
    elif b[1] == flag and b[2] == flag:
        print("fox and goose can`t be both on one side")
        return False
    elif b[2] == flag and b[3] == flag:
        print("goose and corn can`t be both on one side")
        return False
    # not forbiden
    else:
        return True
    # else:
    #     return True

# option 1 - boat: lion / fox / goose / corn
def trans_1(c, i, at):
    old = c.copy()
    c[i] = not c[i]
    # at_bank = True
    if not_forbiden_chek(c, at):
        print("\nRelocating ", meaning[i])
        # print("next state is", c)
        result.append(c)
        return c
    else:
        print("oops")
        return old

# option 2 - boat: goose and corn / fox and corn
def trans_2(c, i, j, at):
    # check if at the same bank
    old = c.copy()
    if c[i] == c[j]:
        c[i] = not c[i]
        c[j] = not c[j]
        # at_bank = True
        if not_forbiden_chek(c, at):
            print("\nRelocating ", meaning[i], " and ", meaning[j])
            # print("next state is", c)
            result.append(c)
            return c
        else:
            print("oops")
            return old

def RBFS(cur, pos):
    next_s = cur.copy()

    # working secuence
    pos = not pos
    next_s = trans_2(next_s, 1, 3, pos)
    pos = not pos
    pos = not pos
    next_s = trans_1(next_s, 0, pos)
    pos = not pos
    next_s = trans_1(next_s, 1, pos)
    pos = not pos
    next_s = trans_1(next_s, 2, pos)
    pos = not pos
    next_s = trans_1(next_s, 3, pos)
    pos = not pos
    next_s = trans_2(next_s, 1, 3, pos)

def driver():
    at_bank = False
    print("RBFS")
    cur_state = bank    # initialising
    RBFS(cur_state, at_bank)
    print("Result: ", result)

driver()



# class State:
#     count = 0
#     lion = False
#     fox = False
#     goose = False
#     corn = False
#     at_bank = False
#     def __init__(self, l,  f, g, c, b):
#         State.count += 1
#         self.lion = l
#         self.fox = f
#         self.goose  = g
#         self.corn = c
#         self.at_bank = b

# result = []
# root =  State(False, False, False, False, False)
# result.append(root)

# def not_forbiden_check(s):
#     flag = not s.at_bank
#     if s.lion == flag and s.fox == flag:
#         print("lion and fox can`t be both on one side")
#         return False
#     elif s.fox == flag and s.goose == flag:
#         print("fox and goose can`t be both on one side")
#         return False
#     elif s.goose == flag and s.corn == flag:
#         print("goose and corn can`t be both on one side")
#         return False
#     # not forbiden
#     else:
#         return True

# def success(s):
#     if s.lion == True and s.fox == True and  s.goose  == True and s.corn  == True:
#         return True
#     else:
#         return False

# # option 2 - boat: goose and corn / fox and corn
# def trans_2(s, i, j):
#     # check if at the same bank
#     old = s.copy()
#     if c[i] == c[j]:
#         c[i] = not c[i]
#         c[j] = not c[j]
#         at_bank = True
#         if not_forbiden_chek(c, at_bank):
#             print("\nRelocating ", meaning[i], " and ", meaning[j])
#             # print("next state is", c)
#             result.append(c)
#             return c
#         else:
#             print("oops")
#             return old

# def create_new(s):
#     i = 0
#     if not success(s):
#         if s.lion == False:

#         new_s = State()

# check(root)

######################