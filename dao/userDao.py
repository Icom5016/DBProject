class UserDAO:
    def __init__(self):
        #[user id, first name, last name, email, phone, username, password]
        U1 = [117, "John", "Green", "john.green@unsc.edu", "7871177609", "MasterChief", "cortana"]
        U2 = [34, "Sam", "McDonald", "sam.mcdonald@unsc.edu", "7870346348", "BlueTwo", "shaddock"]
        U3 = [87, "Kelly", "Reynolds", "kelly.reynolds@unsc.edu", "7870879876", "BlueThree", "reach"]
        U4 = [10, "Catherine", "Halsey", "catherine.halsey@unsc.edu", "7870102345", "DrHalsey", "hellooni"]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

    def getAllUser(self):
        return self.data

    def getUserById(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r
        return None

    def getFNameByUserId(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r[1]
        return None

    def getLNameByUserId(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r[2]
        return None

    def getEmailByUserId(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r[3]
        return None

    def getPhoneByUserId(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r[4]
        return None

    def getUsernameByUserId(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r[5]
        return None

    def getPasswordByUserId(self, user_id):
        for r in self.data:
            if user_id == r[0]:
                return r[6]
        return None