from node import Node
from rbfs import RBFS

def main():
    init_state = Node(False, False, False, False, False)
    goal_state = Node(True, True, True, True, True)
    generated = init_state.move()
    solution = RBFS(init_state, goal_state)

if __name__ == "__main__":
    main()