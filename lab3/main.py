from node import Node

def main():
    init_state = Node([False, False, False, False, False, False, False, False, False, False], False)
    goal_state = Node([True, True, True, True, True, True, True, True, True, True], True)
    print("init - ", init_state.score)
    print("goal - ", goal_state.score)
    solution = init_state.move()

if __name__ == "__main__":

    main()