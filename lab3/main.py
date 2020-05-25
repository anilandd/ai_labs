from node import Node

def main():
    init_state = Node([False, False, False, False, False, False, False, False, False, False], False)
    goal_state = Node([True, True, True, True, True, True, True, True, True, True], True)
    print("init - ", init_state.bank1)
    print("goal - ", goal_state.bank1)

    solution = init_state.move()
    print("solution: \n")
    for s in solution:
        print("\nbank 1: ", s.bank1, "\nbank 2: ", s.bank2)


if __name__ == "__main__":

    main()