def RBFS(init_state, goal_state):
    visited = []
    path = [init_state]
    # while path:

    if init_state == goal_state:
        print("Found!")
    else:
        print("Not found!")
    return None