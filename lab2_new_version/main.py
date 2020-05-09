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
    print("\n-----3 iteration")
    if generated2[2].farmer == False:
        print("1->2")
    else:
        print("2->1")
    generated3 = generated2[2].move()
    print("\n-----4 iteration")
    if generated3[0].farmer == False:
        print("1->2")
    else:
        print("2->1")
    generated4 = generated3[0].move()
    print("\n-----5 iteration")
    if generated4[2].farmer == False:
        print("1->2")
    else:
        print("2->1")
    generated5 = generated4[2].move()
    print("\n-----6 iteration")
    if generated5[0].farmer == False:
        print("1->2")
    else:
        print("2->1")
    generated6 = generated4[0].move()
    solution = RBFS(init_state, goal_state)

if __name__ == "__main__":
    main()