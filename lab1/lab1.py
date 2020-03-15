max_jar1 = 5
max_jar2 = 3
goals = [[4,0],[4,3]]
dead_end = [[0,0], [max_jar1,max_jar2]]
cur_state = [0,0] # current state of jar1 and jar2
# branch = [cur_state]
history = [cur_state]

def fill_j1(cur_state):
    next_state = [max_jar1, cur_state[1]]
    return next_state

def fill_j2(cur_state):
    next_state = [cur_state[0], max_jar2]
    return next_state

def pour_j1(cur_state):
    next_state = [0, cur_state[1]]
    return next_state

def pour_j2(cur_state):
    next_state = [cur_state[0], 0]
    return next_state

def from_j1_to_j2(cur_state):
    dif2 = max_jar2 - cur_state[1]
    if dif2 >= cur_state[0]:
        next_state = [0, cur_state[1] + cur_state[0]]
    else:
        next_state = [cur_state[0] - dif2, cur_state[1] + dif2]
    return next_state

def from_j2_to_j1(cur_state):
    dif1 = max_jar1 - cur_state[0]
    if dif1 >= cur_state[1]:
        next_state = [cur_state[0] + cur_state[1], 0]
    else:
        next_state = [cur_state[0] + dif1, cur_state[1] - dif1]
    return next_state    

def util_add(cur_state, branch):
    if not(cur_state in branch) and not(cur_state in dead_end) and not(cur_state in history):
        branch.append(cur_state)
        print(branch)
        return cur_state
    else:
        return branch[-1]


def search(cur_state):
    branch = [cur_state]
    rem = cur_state
    while not(cur_state in goals):
    
        if (cur_state[0] != max_jar1) and (cur_state[1] != max_jar2):
            cur_state = fill_j1(cur_state)
            cur_state = util_add(cur_state, branch)

        if (cur_state[0] != max_jar1) and (cur_state[1] != max_jar2):
            cur_state = fill_j2(cur_state)
            cur_state = util_add(cur_state, branch)
    
        if not(cur_state in dead_end) and ((cur_state[0] >= 0) and (cur_state[1] != 0)):
            cur_state = pour_j1(cur_state)
            cur_state = util_add(cur_state, branch)

        if not(cur_state in dead_end) and ((cur_state[1] >= 0) and (cur_state[0] != 0)):
            cur_state = pour_j2(cur_state)
            cur_state = util_add(cur_state, branch)

        if (cur_state != [0,0]) and (cur_state != [5,3]):
            if cur_state[0] != 0 and cur_state[1] != max_jar2:
                cur_state = from_j1_to_j2(cur_state)
                cur_state = util_add(cur_state, branch)
            if cur_state[0] != max_jar1 and cur_state[1] != 0:
                cur_state = from_j2_to_j1(cur_state)
                cur_state = util_add(cur_state, branch)
        if cur_state == rem:
            break

    if branch != history:
        print("new solution: ", branch)

    return branch

def dfs ():
    i = len(history) - 1 
    while i >= 0:
        new_branch = []
        new_branch = search(history[i])
        i -= 1

    
history = search(cur_state)
print("Best solution found: ", history, " - ", len(history) - 1, " steps found")
print("-------------------------------------------------------------------------------------------------------------")
# branch = []
# branch.append([2,3])
# branch  = search(branch[0])
dfs()

