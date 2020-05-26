from node import Node
from TABU import TABU
import sys

sys.setrecursionlimit(10**6) 

def main():
    init_state = Node([False, False, False, False, False, False, False, False, False, False], False)
    goal_state = Node([True, True, True, True, True, True, True, True, True, True], True)

    TABU(init_state, goal_state, [init_state], [init_state])



if __name__ == "__main__":

    main()