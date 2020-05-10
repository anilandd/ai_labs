from node import Node
from rbfs import RBFS

def main():
    init_state = Node(False, False, False, False, False)
    goal_state = Node(True, True, True, True, True)
    RBFS(init_state, goal_state, [init_state], [])


if __name__ == "__main__":

    main()