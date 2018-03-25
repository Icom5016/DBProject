from dao.userDao import UserDAO

class ContactListDAO:
    def __init__(self):
        #[contact id, contactlist owner id, contact(user) id]
        Co1 = [200, 117, 34] #John is owner
        Co2 = [201, 117, 87]
        Co3 = [202, 117, 10]
        Co4 = [203, 34, 117] #Sam is owner
        Co5 = [204, 34, 87]
        Co6 = [205, 87, 117] #Kelly is owner
        Co7 = [206, 87, 34]
        Co8 = [207, 10, 117] #Halsey is owner

        self.data = []
        self.data.append(Co1)
        self.data.append(Co2)
        self.data.append(Co3)
        self.data.append(Co4)
        self.data.append(Co5)
        self.data.append(Co6)
        self.data.append(Co7)
        self.data.append(Co8)

    #returns all of the contact lists
    def getAllContactList(self):
        dao = UserDAO()
        result = []
        ownerId = 0
        contacts = []
        for r in self.data:
            if ownerId != r[1]:
                ownerId = r[1]
                for r2 in self.data:
                    if ownerId == r2[1]:
                        contactId = r2[2]
                        contacts.append(dao.getUserById(contactId))
                result.append([ownerId, contacts])
                contacts = []
        if result == []:
            return None
        return result

    #returns single contact list... Various id will return the same list if the beling to the same owner
    #Not sure si debe ir. No tiene mucho sentido since there's no single Id para un list completo de contacts
    # def getContactListByID(self, id):
    #     dao = UserDAO()
    #     result = []
    #     ownerId = 0
    #     contacts = []
    #     for r in self.data:
    #         if ownerId != r[1]:
    #             ownerId = r[1]
    #             for r2 in self.data:
    #                 if ownerId == r2[1]:
    #                     contactId = r2[2]
    #                     contacts.append(dao.getUserById(contactId))
    #             result.append([ownerId, contacts])
    #             contacts = []
    #     if result == []:
    #         return None
    #     return result

    #returns single contact list
    def getContactListByUserID(self, id):
        dao = UserDAO()
        result = []
        ownerId = id
        contacts = []
        for r in self.data:
            if ownerId == r[1]:
                contactId = r[2]
                contacts.append(dao.getUserById(contactId))
        result.append(ownerId)
        result.append(contacts)
        if contacts == []:
            return None
        return result

    #returns the user attributes of an existing contact of any list
    def getSingleContactByUserID(self, id):
        dao = UserDAO()
        result = []
        contactId = id
        for r in self.data:
            if contactId == r[2]:
                return dao.getUserById(contactId)
        return None