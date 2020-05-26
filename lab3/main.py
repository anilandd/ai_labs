from node import Node
from TABU import TABU

def main():
    init_state = Node([False, False, False, False, False, False, False, False, False, False], False)
    goal_state = Node([True, True, True, True, True, True, True, True, True, True], True)
    # print("init - ", init_state.bank1)
    # print("goal - ", goal_state.bank1)

    TABU(init_state, goal_state, [init_state], [])

    # solution = init_state.move()
    # print("solution: \n")
    # i = 1
    # for s in solution:
    #     print("\nvariant ", i)
    #     print("people: ", s.people)
    #     print("boat: ", s.boat)
    #     i += 1


if __name__ == "__main__":

    main()