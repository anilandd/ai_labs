# people = [0-m1, 1-w1, 2-m2, 3-w2, 4-m3, 5-w3, 6-m4, 7-w4, 8-m5, 9-w5]

class Node:
    def __init__(self, people, boat, parent = None):
        self.people = people
        self.boat = boat
        self.parent = parent
        self.score = self.countScore()
        # self.m1 = m1
        # self.m2 = m2
        # self.m3 = m3
        # self.m4 = m4
        # self.m5 = m5
        # self.w1 = w1
        # self.w2 = w2
        # self.w3 = w3
        # self.w4 = w4
        # self.w5 = w5


    def countScore(self):
        s = 0
        for p in self.people:
            if p == True:
                s += 1
        return s
        # if self.m1 == True:
        #     s += 1
        # if self.m2 == True:
        #     s += 1
        # if self.m3 == True:
        #     s += 1
        # if self.m4 == True:
        #     s += 1
        # if self.m5 == True:
        #     s += 1
        # if self.w1 == True:
        #     s += 1
        # if self.w2 == True:
        #     s += 1
        # if self.w3 == True:
        #     s += 1
        # if self.w4 == True:
        #     s += 1
        # if self.w5 == True:
        #     s += 1

    def move(self):

        new_states = []

        if self.boat == self.people[0]:
            new_states.append(self.moveM1())

        if self.boat == self.people[2]:
            new_states.append(self.moveM2())

        if self.boat == self.people[4]:
            new_states.append(self.moveM3())

        return new_states
    
    def moveM1(self):
        return Node(
            [not self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )

    def moveM2(self):
        return Node(
            [self.people[0], self.people[1], 
            not self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )
    
    def moveM3(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            not self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )
    
    def moveM4(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            not self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )
    
    def moveM5(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            not self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )

    def moveW1(self):
        return Node(
            [self.people[0], not self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )

    def moveW2(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], not self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )
    
    def moveW3(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], not self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )
    
    def moveW4(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], not self.people[7], 
            self.people[8], self.people[9]],
            not self.boat,
            parent = self
        )
    
    def moveW5(self):
        return Node(
            [self.people[0], self.people[1], 
            self.people[2], self.people[3], 
            self.people[4], self.people[5], 
            self.people[6], self.people[7], 
            self.people[8], not self.people[9]],
            not self.boat,
            parent = self
        )
