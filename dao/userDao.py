class UserDAO:
    def __init__(self):
        #[user id, first name, last name, email, phone]
        U1 = [117, "John", "Chief", "master.chief@unsc.edu", "7871177609"]
        U2 = [34, "Sam", "Two", "sam.two@unsc.edu", "7870346348"]
        U3 = [87, "Kelly", "Three", "kelly.three@unsc.edu", "7870879876"]
        U4 = [10, "Catherine", "Halsey", "catherine.halsey@unsc.edu", "7870102345"]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

    def getAllUser(self):
        return self.data

    def getUserById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getFNameByUserId(self, id):
        print("DEBUG - userDao")
        for r in self.data:
            if id == r[0]:
                return r[1]
        return None

    def getLNameByUserId(self, id):
        for r in self.data:
            if id == r[0]:
                return r[2]
        return None

    def getEmailByUserId(self, id):
        for r in self.data:
            if id == r[0]:
                return r[3]
        return None

    def getPhoneByUserId(self, id):
        for r in self.data:
            if id == r[0]:
                return r[4]
        return None