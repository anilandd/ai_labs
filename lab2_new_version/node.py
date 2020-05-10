# False represents first bank / True represents second bank 

class Node:
    def __init__(self, l, f, g, c, farm, par = None):
        self.lion = l
        self.fox = f
        self.goose = g
        self.corn = c
        self.farmer = farm
        self.parent = par
        self.fVal = self.countF()   # number of items at the first bank

    def countF(self):
        f_count = 0
        if self.lion == False:
            f_count +=1
        if self.fox == False:
            f_count +=1
        if self.goose == False:
            f_count +=1
        if self.corn == False:
            f_count +=1 
        return f_count

    def move(self):
        states = []

        # fox
        print("\n? moving fox")
        if self.fox == self.farmer and self.not_forbidden(self.moveFox()):
            print("! moving fox")
            states.append(self.moveFox())

        # goose
        print("\n? moving goose")
        if self.goose == self.farmer and self.not_forbidden(self.moveGoose()):
            print("! moving goose")
            states.append(self.moveGoose())

        # lion
        print("\n? moving lion")
        if self.lion == self.farmer and self.not_forbidden(self.moveLion()):
            print("! moving lion")
            states.append(self.moveLion())

        # corn
        print("\n? moving corn")
        if self.corn == self.farmer and self.not_forbidden(self.moveCorn()):
            print("! moving corn")
            states.append(self.moveCorn())

        # goose and corn
        print("\n? moving goose and corn")
        if self.goose == self.corn == self.farmer and self.not_forbidden(self.moveGooseCorn()):
            print("! moving goose and corn")
            states.append(self.moveGooseCorn())

        # fox and corn
        print("\n? moving fox and corn")
        if self.fox == self.corn == self.farmer and self.not_forbidden(self.moveFoxCorn()):
            print("! moving fox and corn")
            states.append(self.moveFoxCorn())

        # going back emptyhanded
        print("\n? going back emptyhanded")
        if self.canLeave():
            print("! going back emptyhanded")
            states.append(self.leave())

        return states

    def not_forbidden(self, possible_state):

        if not self.parent or self.parent != possible_state:
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
        else:
            return False

    def moveLion(self):
        return Node(
            not self.lion,
            self.fox,
            self.goose,
            self.corn,
            not self.farmer,
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

    def canLeave(self):
        if self.farmer:
            if self.lion == self.corn == True and self.fox == self.goose == False:
                return True
            elif self.lion == self.goose == True and self.fox == self.corn == False:
                return True
            elif self.fox == self.corn == True and self.lion == self.goose == False:
                return True
            else:
                return False

    def leave(self):
        return Node(
            self.lion,
            self.fox,
            self.goose,
            self.corn,
            not self.farmer,
            par = self
        )

    def __eq__(self, other):
        return (self.lion == other.lion and
                self.fox == other.fox and
                self.goose == other.goose and
                self.corn == other.corn)
