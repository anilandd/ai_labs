from node import Node
from rbfs import RBFS

def main():
    init_state = Node(False, False, False, False, False)
    goal_state = Node(True, True, True, True, True)
    print("\n-----1 iteration")
    if init_state.farmer == False:
        print("1->2")
    else:
        print("2->1")
    generated1 = init_state.move()
    print("\n-----2 iteration")
    if generated1[0].farmer == False:
        print("1->2")
    else:
        print("2->1")
    generated2 = generated1[0].move()
    solution = RBFS(init_state, goal_state)

if __name__ == "__main__":
    main()