# False represents first bank / True represents second bank 

class Node:
    def __init__(self, l, f, g, c, farm, par = None):
        self.lion = l
        self.fox = f
        self.goose = g
        self.corn = c
        self.farmer = farm
        self.parent = par
        self.fVal = 0

    def move(self):
        states = []

        # lion
        print("\n? moving lion")
        if self.not_forbidden(self.moveLion()):
            print("! moving lion")
            states.append(self.moveLion())

        # fox
        print("\n? moving fox")
        if self.not_forbidden(self.moveFox()):
            print("! moving fox")
            states.append(self.moveFox())

        # goose
        print("\n? moving goose")
        if self.not_forbidden(self.moveGoose()):
            print("! moving goose")
            states.append(self.moveGoose())

        # corn
        print("\n? moving corn")
        if self.not_forbidden(self.moveCorn()):
            print("! moving corn")
            states.append(self.moveCorn())

        # goose and corn
        print("\n? moving goose and corn")
        if self.not_forbidden(self.moveGooseCorn()):
            print("! moving goose and corn")
            states.append(self.moveGooseCorn())

        #fox and corn
        print("\n? moving fox and corn")
        if self.not_forbidden(self.moveFoxCorn()):
            print("! moving fox and corn")
            states.append(self.moveFoxCorn())

        return states

    def not_forbidden(self, possible_state):
        stay = not possible_state.farmer
        if possible_state.lion == stay and possible_state.fox == stay:
            print("-lion and fox can`t be both on one side")
            return False
        elif possible_state.fox == stay and possible_state.goose == stay:
            print("-fox and goose can`t be both on one side")
            return False
        elif possible_state.goose == stay and possible_state.corn == stay:
            print("-goose and corn can`t be both on one side")
            return False
        else:
            return True   

    def moveLion(self):
        return Node(
            not self.lion,
            self.fox,
            self.goose,
            self.corn,
            True,
            par = self
        )

    def moveFox(self):
        return Node(
            self.lion,
            not self.fox,
            self.goose,
            self.corn,
            not self.farmer,
            par = self
        )
    
    def moveGoose(self):
        return Node(
            self.lion,
            self.fox,
            not self.goose,
            self.corn,
            not self.farmer,
            par = self
        )

    def moveCorn(self):
        return Node(
            self.lion,
            self.fox,
            self.goose,
            not self.corn,
            not self.farmer,
            par = self
        )

    def moveGooseCorn(self):
        return Node(
            self.lion,
            self.fox,
            not self.goose,
            not self.corn,
            not self.farmer,
            par = self
        )   

    def moveFoxCorn(self):
        return Node(
            self.lion,
            not self.fox,
            self.goose,
            not self.corn,
            not self.farmer,
            par = self
        )
