# people = [0-m1, 1-w1, 2-m2, 3-w2, 4-m3, 5-w3, 6-m4, 7-w4, 8-m5, 9-w5]

boat_capacity = 3
couples = 5
number_of_people = couples * 2

class Node:
    def __init__(self, people, boat, parent = None):
        self.people = people
        self.boat = boat
        # self.bank1 = self.onBank1()
        # self.bank2 = self.onBank2()
        self.parent = parent
        self.score = self.countScore()


    # def onBank1(self):
    #     bank1 = []
    #     p = 0
    #     while p < len(self.people):
    #         if self.people[p] == False:
    #             bank1.append(p)
    #         p += 1
    #     return bank1


    # def onBank2(self):
    #     bank2 = []
    #     p = 0
    #     while p < len(self.people):
    #         if self.people[p] == True:
    #             bank2.append(p)
    #         p += 1
    #     return bank2


    def countScore(self):
        s = 0
        for p in self.people:
            if p == True:
                s += 1
        return s


    def move(self):

        new_states = []

        i = 0
        while i < number_of_people:
            # generating moving of 1 person
            if self.boat == self.people[i] and self.is_not_forbidden(self.moveOnePerson(i)):
                new_states.append(self.moveOnePerson(i))
                j = 0
                while j < number_of_people:
                    # generating moving of 2 persons
                    if i != j and self.boat == self.people[j] and self.is_not_forbidden(self.moveTwoPersons(i, j)):
                        new_states.append(self.moveTwoPersons(i, j))
                        k = 0
                        while k < number_of_people:
                            # generating moving of 3 persons
                            if i != k and j != k and self.boat == self.people[k] and self.is_not_forbidden(self.moveThreePersons(i, j, k)):
                                new_states.append(self.moveThreePersons(i, j, k))
                            k += 1
                    j += 1
            i += 1

        return new_states


    def is_not_forbidden(self, possible_state):

        women_indexes = [1, 3, 5, 7, 9]
        men_indexes = [0, 2, 4, 6, 8]

        for wi in women_indexes:
            if possible_state.people[wi] != possible_state.people[wi-1]:
                other_men = men_indexes.copy()
                other_men.remove(wi-1)
                for om in other_men:
                    if possible_state.people[wi] == possible_state.people[om]:
                        return False
            else:
                continue
        return True
    

    def moveOnePerson(self, person):
        new_people = self.people.copy()
        new_people[person] = not new_people[person]
        return Node(
            new_people,
            not self.boat,
            parent = self
        )

    def moveTwoPersons(self, person1, person2):
        new_people = self.people.copy()
        new_people[person1] = not new_people[person1]
        new_people[person2] = not new_people[person2]
        return Node(
            new_people,
            not self.boat,
            parent = self
        )

    def moveThreePersons(self, person1, person2, person3):
        new_people = self.people.copy()
        new_people[person1] = not new_people[person1]
        new_people[person2] = not new_people[person2]
        new_people[person3] = not new_people[person3]
        return Node(
            new_people,
            not self.boat,
            parent = self
        )








    # def move1(self):

    #     new_states = []

    #     in_boat = 0

    #     # if self.boat:
    #     #     for p in self.bank2:
    #     #         new_states.append(self.moveM1())
    #     # else:
    #     #     for p in self.bank1:
    #     #         new_states.append(self.moveM1())

    #     # for p in self.people:
    #     #     if p == self.boat:

    #     if self.boat == self.people[0] and self.is_not_forbidden(self.moveM1(not self.boat)):
    #         new_states.append(self.moveM1(not self.boat))
    #     if self.boat == self.people[1] and self.is_not_forbidden(self.moveW1(not self.boat)):
    #         new_states.append(self.moveW1(not self.boat))
    #     if self.boat == self.people[2] and self.is_not_forbidden(self.moveM2(not self.boat)):
    #         new_states.append(self.moveM2(not self.boat))
    #     if self.boat == self.people[3] and self.is_not_forbidden(self.moveW2(not self.boat)):
    #         new_states.append(self.moveW2(not self.boat))
    #     if self.boat == self.people[4] and self.is_not_forbidden(self.moveM3(not self.boat)):
    #         new_states.append(self.moveM3(not self.boat))
    #     if self.boat == self.people[5] and self.is_not_forbidden(self.moveW3(not self.boat)):
    #         new_states.append(self.moveW3(not self.boat))
    #     if self.boat == self.people[6] and self.is_not_forbidden(self.moveM4(not self.boat)):
    #         new_states.append(self.moveM4(not self.boat))
    #     if self.boat == self.people[7] and self.is_not_forbidden(self.moveW4(not self.boat)):
    #         new_states.append(self.moveW4(not self.boat))
    #     if self.boat == self.people[8] and self.is_not_forbidden(self.moveM5(not self.boat)):
    #         new_states.append(self.moveM5(not self.boat))
    #     if self.boat == self.people[9] and self.is_not_forbidden(self.moveW5(not self.boat)):
    #         new_states.append(self.moveW5(not self.boat))

    #     # if self.boat == self.people[0] and self.is_not_forbidden(self.moveM1(not self.boat)) and not (self.moveM1(not self.boat) in new_states):
    #     #     new_states.append(self.moveM1(not self.boat))
    #     # if self.boat == self.people[1] and self.is_not_forbidden(self.moveW1(not self.boat)) and not (self.moveW1(not self.boat) in new_states):
    #     #     new_states.append(self.moveW1(not self.boat))
    #     # if self.boat == self.people[2] and self.is_not_forbidden(self.moveM2(not self.boat)) and not (self.moveM2(not self.boat) in new_states):
    #     #     new_states.append(self.moveM2(not self.boat))
    #     # if self.boat == self.people[3] and self.is_not_forbidden(self.moveW2(not self.boat)) and not (self.moveW2(not self.boat) in new_states):
    #     #     new_states.append(self.moveW2(not self.boat))
    #     # if self.boat == self.people[4] and self.is_not_forbidden(self.moveM3(not self.boat)) and not (self.moveM3(not self.boat) in new_states):
    #     #     new_states.append(self.moveM3(not self.boat))
    #     # if self.boat == self.people[5] and self.is_not_forbidden(self.moveW3(not self.boat)) and not (self.moveW3(not self.boat) in new_states):
    #     #     new_states.append(self.moveW3(not self.boat))
    #     # if self.boat == self.people[6] and self.is_not_forbidden(self.moveM4(not self.boat)) and not (self.moveM4(not self.boat) in new_states):
    #     #     new_states.append(self.moveM4(not self.boat))
    #     # if self.boat == self.people[7] and self.is_not_forbidden(self.moveW4(not self.boat)) and not (self.moveW4(not self.boat) in new_states):
    #     #     new_states.append(self.moveW4(not self.boat))
    #     # if self.boat == self.people[8] and self.is_not_forbidden(self.moveM5(not self.boat)) and not (self.moveM5(not self.boat) in new_states):
    #     #     new_states.append(self.moveM5(not self.boat))
    #     # if self.boat == self.people[9] and self.is_not_forbidden(self.moveW5(not self.boat)) and not (self.moveW5(not self.boat) in new_states):
    #     #     new_states.append(self.moveW5(not self.boat))

    #     # while in_boat < boat_capacity:



    #     # if self.boat == self.people[0]:
    #     #     new_states.append(self.moveM1())

    #     # if self.boat == self.people[2]:
    #     #     new_states.append(self.moveM2())

    #     # if self.boat == self.people[4]:
    #     #     new_states.append(self.moveM3())

    #     return new_states1




    # def moveM1(self, b):
    #     return Node(
    #         [not self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )

    # def moveM2(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         not self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
    
    # def moveM3(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         not self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
    
    # def moveM4(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         not self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
    
    # def moveM5(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         not self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )

    # def moveW1(self, b):
    #     return Node(
    #         [self.people[0], not self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )

    # def moveW2(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], not self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
    
    # def moveW3(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], not self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
    
    # def moveW4(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], not self.people[7], 
    #         self.people[8], self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
    
    # def moveW5(self, b):
    #     return Node(
    #         [self.people[0], self.people[1], 
    #         self.people[2], self.people[3], 
    #         self.people[4], self.people[5], 
    #         self.people[6], self.people[7], 
    #         self.people[8], not self.people[9]],
    #         boat = b,
    #         parent = self
    #     )
