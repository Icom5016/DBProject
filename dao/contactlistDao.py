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
        owner_id = 0
        contacts = []
        for r in self.data:
            if owner_id != r[1]:
                owner_id = r[1]
                for r2 in self.data:
                    if owner_id == r2[1]:
                        contact_id = r2[2]
                        contacts.append(dao.getUserById(contact_id))
                result.append([owner_id, contacts])
                contacts = []
        if result == []:
            return None
        return result

    #returns single contact list
    def getContactListByUserID(self, user_id):
        dao = UserDAO()
        result = []
        owner_id = user_id
        contacts = []
        for r in self.data:
            if owner_id == r[1]:
                contact_id = r[2]
                contacts.append(dao.getUserById(contact_id))
        result.append(owner_id)
        result.append(contacts)
        if contacts == []:
            return None
        return result

    #returns the user attributes of an existing contact of any list
    def getSingleContactByUserID(self, user_id):
        dao = UserDAO()
        result = []
        contact_id = user_id
        for r in self.data:
            if contact_id == r[2]:
                return dao.getUserById(contact_id)
        return None