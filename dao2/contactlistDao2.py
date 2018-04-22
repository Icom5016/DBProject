from dao2.userDao2 import UserDAO
from config.dbconfig import pg_config
import psycopg2

class ContactListDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

        # #[contact id, contactlist owner id, contact(user) id]
        # Co1 = [200, 117, 34] #John is owner
        # Co2 = [201, 117, 87]
        # Co3 = [202, 117, 10]
        # Co4 = [203, 34, 117] #Sam is owner
        # Co5 = [204, 34, 87]
        # Co6 = [205, 87, 117] #Kelly is owner
        # Co7 = [206, 87, 34]
        # Co8 = [207, 10, 117] #Halsey is owner
        #
        # self.data = []
        # self.data.append(Co1)
        # self.data.append(Co2)
        # self.data.append(Co3)
        # self.data.append(Co4)
        # self.data.append(Co5)
        # self.data.append(Co6)
        # self.data.append(Co7)
        # self.data.append(Co8)

    #returns all of the contact lists
    def getAllContactList(self):
        cursor = self.conn.cursor()
        query = "select L.clist_id, L.person_id, C.person_id from contact_list as L, " \
                "contacts as C where L.clist_id = C.clist_id;"
        cursor.execute(query)
        dao = UserDAO()
        result = []
        clist_id = 0
        contacts = []

        #Save the data of the cursor to be able to iterate through it multiple times later
        cursor_result = []
        for row in cursor:
            cursor_result.append(row)

        for row in cursor_result:
            if clist_id != row[0]:
                clist_id = row[0]
                owner_id = row[1]
                for row2 in cursor_result:
                    if owner_id == row2[1]:
                        contact_id = row2[2]
                        contacts.append(dao.getUserById(contact_id))
                result.append([clist_id, owner_id, contacts])
                contacts = []
        if result == []:
            return None
        return result

    #returns the contact list info
    def getContactListByID(self, clist_id):
        cursor = self.conn.cursor()
        query = "select L.clist_id, L.person_id, C.person_id from contact_list as L, " \
                "contacts as C where L.clist_id = C.clist_id and L.clist_id = %s;"
        cursor.execute(query, (clist_id,))
        dao = UserDAO()
        result = []
        clist_id = 0
        owner_id = 0
        contacts = []
        firstPass = True
        for row in cursor:
            if firstPass:
                clist_id = row[0]
                owner_id = row[1]
            contacts.append(dao.getUserById(row[2]))
        # result.append([clist_id, owner_id, contacts])
        result.append(clist_id)
        result.append(owner_id)
        result.append(contacts)
        if result == []:
            return None
        return result

    #returns single contact list
    def getContactListByUserID(self, user_id):
        cursor = self.conn.cursor()
        query = "select L.clist_id, L.person_id, C.person_id from contact_list as L, " \
                "contacts as C where L.clist_id = C.clist_id and L.person_id = %s;"
        cursor.execute(query, (user_id,))

        dao = UserDAO()
        result = []
        clist_id = 0
        owner_id = 0
        contacts = []
        firstPass = True
        for row in cursor:
            if firstPass:
                clist_id = row[0]
                owner_id = row[1]
            contacts.append(dao.getUserById(row[2]))
        # result.append([clist_id, owner_id, contacts])
        result.append(clist_id)
        result.append(owner_id)
        result.append(contacts)
        if result == []:
            return None
        return result

        # dao = UserDAO()
        # result = []
        # owner_id = user_id
        # contacts = []
        # for r in self.data:
        #     if owner_id == r[1]:
        #         contact_id = r[2]
        #         contacts.append(dao.getUserById(contact_id))
        # result.append(owner_id)
        # result.append(contacts)
        # if contacts == []:
        #     return None
        # return result

    #returns the user attributes of an existing contact of any list
    # def getSingleContactByUserID(self, user_id):
    #     dao = UserDAO()
    #     result = []
    #     contact_id = user_id
    #     for r in self.data:
    #         if contact_id == r[2]:
    #             return dao.getUserById(contact_id)
    #     return None