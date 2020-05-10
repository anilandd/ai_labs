meanings = {False: "at first bank  |", True: "at second bank |"}
def RBFS(init_state, goal_state, path, visited):    

    if init_state == goal_state:
        print("\nGoal found!\n")
        print("Trace:\n")
        v = 0
        while v < len(path):
            i = v + 1
            print(i , " - ", "lion", meanings[path[v].lion], "fox",  meanings[path[v].fox], "goose", meanings[path[v].goose], "corn", meanings[path[v].corn])
            v += 1
    else:
        print("\n----------")
        print("State:", init_state.lion, init_state.fox,  init_state.goose, init_state.corn)
        possible = init_state.move()
        if init_state.parent:        
            F_prev = init_state.parent.fVal
        else:
            F_prev = 4

        f_list = []

        i = 0
        while i < len(possible):
            if visited and possible[i] == visited[-1]:
                    possible.remove(possible[i])
                    continue
            f_list.append(possible[i].fVal)
            i += 1

        possible_min_f = min(f_list)
        next_state_index = f_list.index(possible_min_f)

        print("\npossible_min_f: ", possible_min_f)
        print("F_prev: ", F_prev)

        if possible_min_f < F_prev:            
            path.append(possible[next_state_index])   
            RBFS(possible[next_state_index], goal_state, path, visited)
        if possible_min_f == F_prev:
            path.append(possible[next_state_index]) 
            RBFS(possible[next_state_index], goal_state, path, visited)
        if possible_min_f > F_prev:
            print("\nGoing  back to the previous state")
            visited.append(init_state)
            RBFS(path[-2], goal_state, path, visited)
    
