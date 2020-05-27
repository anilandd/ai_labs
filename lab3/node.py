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


    # def countScore(self):
    #     s = 0
    #     for p in self.people:
    #         if p == True:
    #             s += 1
    #     return s

    def countScore(self):
        score = 0
        i = 0
        while i < number_of_people:
            j = i + 1
            if self.people[i] == self.people[j] == True:
                score += 1
            i += 2
        return score


    def move(self):

        new_states = []

        # in_boat = 0
        i = 0
        while i < number_of_people:
            # generating moving of 1 person
            if self.boat == self.people[i]:
                if self.is_not_forbidden(self.moveOnePerson(i)):
                    new_states.append(self.moveOnePerson(i))
                    # in_boat += 1
                    j = 0
                    while j < number_of_people:
                        # generating moving of 2 persons
                        if i != j and self.boat == self.people[j]:
                            if self.is_not_forbidden(self.moveTwoPersons(i, j)):
                                # in_boat += 1
                                new_states.append(self.moveTwoPersons(i, j))
                                k = 0
                                while k < number_of_people:
                                    # generating moving of 3 persons
                                    if i != k and j != k and self.boat == self.people[k] and self.is_not_forbidden(self.moveThreePersons(i, j, k)):
                                        new_states.append(self.moveThreePersons(i, j, k))
                                    k += 1
                            else:
                                check_result = self.canBringPartnerWith2(self.moveTwoPersons(i,j), i, j)
                                if check_result[0]:
                                    for n in check_result[1]:
                                        new_states.append(self.moveThreePersons(i, j, n))
                                        # in_boat += 2
                        j += 1
                else:
                    check_result = self.canBringPartnerWith1(self.moveOnePerson(i), i)
                    if check_result[0]:
                        for n in check_result[1]:
                            new_states.append(self.moveTwoPersons(i, n))
                            # in_boat += 2

                        j = 0
                        while j < number_of_people:
                            # generating moving of 2 persons
                            if i != j and self.boat == self.people[j]:
                                if self.is_not_forbidden(self.moveTwoPersons(i, j)):
                                    # in_boat += 1
                                    new_states.append(self.moveTwoPersons(i, j))
                                    k = 0
                                    while k < number_of_people:
                                        # generating moving of 3 persons
                                        if i != k and j != k and self.boat == self.people[k] and self.is_not_forbidden(self.moveThreePersons(i, j, k)):
                                            new_states.append(self.moveThreePersons(i, j, k))
                                        k += 1
                                else:
                                    check_result = self.canBringPartnerWith2(self.moveTwoPersons(i,j), i, j)
                                    if check_result[0]:
                                        for n in check_result[1]:
                                            new_states.append(self.moveThreePersons(i, j, n))
                                            # in_boat += 2
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

    def canBringPartnerWith2(self, possible_state, p1, p2):
        
        res = []
        ok_indexes = []
        result = []

        flag = not possible_state.people[p1]

        i = 0
        while i < len(possible_state.people):
            if i != p1 and i != p2 and possible_state.people[i] == flag:
                if  self.is_not_forbidden(self.moveThreePersons(p1, p2, i)):
                    if len(res) == 1:
                        res[0] = True
                    else:
                        res.append(True)
                    ok_indexes.append(i)
                    # return result
            i += 1

        if not res:
            res.append(False)

        result.append(res)
        result.append(ok_indexes) 
        return result
                
            
    def canBringPartnerWith1(self, possible_state, p1):
        
        res = []
        ok_indexes = []
        result = []

        flag = not possible_state.people[p1]

        i = 0
        while i < len(possible_state.people):
            if i != p1 and possible_state.people[i] == flag:
                if  self.is_not_forbidden(self.moveTwoPersons(p1, i)):
                    if len(res) == 1:
                        res[0] = True
                    else:
                        res.append(True)
                    ok_indexes.append(i)
                    # return result
            i += 1

        if not res:
            res.append(False)

        result.append(res)
        result.append(ok_indexes) 

        return result

    

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

    def __eq__(self, other):
        if other:
            return (self.people == other.people and
                    self.boat == other.boat)
        else:
            return False