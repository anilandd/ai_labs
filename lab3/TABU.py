def TABU(init_state, goal_state, path, tabu):
    
    # new_local_best = init_state

    if init_state == goal_state:
        print("\nGoal found!\n")
        print("Trace:\n")
        v = 0
        while v < len(path):
            i = v + 1
            print(i , " - people : ", path[v].people, " | boat : ", path[v].boat)
            v += 1
    else:
        print("\n----------")
        print("State:", init_state.people)
        if tabu:
            print("Tabu: ", len(tabu))

        possible = init_state.move()

        s_list = []

        j = 0
        while j < len(possible):
            s_list.append(possible[j].score)
            j += 1

        local_best = selection(s_list, possible, tabu, path)
        if local_best == None:
            local_best = new_local_best
        
        TABU(local_best, goal_state, path, tabu)


def selection(s_list, possible, tabu, path):

    if len(s_list) != 0:
        possible_max_score = max(s_list)
        next_state_index = s_list.index(possible_max_score)

        if tabu_check(possible[next_state_index], tabu):
            print("max_score: ", possible_max_score)
            tabu.append(possible[next_state_index])
            path.append(possible[next_state_index])
            global new_local_best
            new_local_best = possible[next_state_index]
            return possible[next_state_index]
        else:
            # tabu.append(possible[next_state_index])
            s_list.remove(s_list[next_state_index])
            possible.remove(possible[next_state_index])
            selection(s_list, possible, tabu, path)
    else:
        print("\n\n!!! new cicle")
        path.pop()
        # global new_local_best
        new_local_best = path[-1]
        return path[-1]




def tabu_check(best, tabu):
    for t in tabu:
        if best.people == t.people and best.boat == best.boat:
            return False
    return True


        # if tabu:
        #     i = 0 
        #     while i < len(possible):
        #         for t in tabu:
        #             # print("i - ", i, " len - ", len(possible))
        #             if possible[i].people == t.people:
        #                 if possible[i].boat == t.boat:
        #                     possible.remove(possible[i])
        #                     if len(possible) == i:
        #                         break
        #                     else:
        #                         continue
        #         # print("\n")
        #         i += 1