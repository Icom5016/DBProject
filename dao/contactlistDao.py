from dao.userDao import UserDAO
from config.dbconfig import pg_config
import psycopg2

class ContactListDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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

    def getContactsByUserID(self, user_id):
        cursor = self.conn.cursor()
        query = "select C.person_id from contact_list as L, " \
               "contacts as C where L.clist_id = C.clist_id and L.person_id = %s;"
        cursor.execute(query, (user_id,))

        dao = UserDAO()
        result = []
        clist_id = 0
        owner_id = 0
        contacts = []
        for row in cursor:
            result.append(dao.getUserById(row[0]))
        if result == []:
            return None
        return result

    def insertContactList(self, person_id):
        cursor = self.conn.cursor()
        query = "insert into contact_list(person_id) " \
                "values (%s) returning clist_id;"
        cursor.execute(query, (person_id,))
        clist_id = cursor.fetchone()[0]
        self.conn.commit()
        return clist_id

    def insertContact(self, clist_id, person_id):
        cursor = self.conn.cursor()
        query = "insert into contacts(clist_id, person_id) " \
                "values (%s, %s) returning contact_id;"
        cursor.execute(query, (clist_id, person_id,))
        contact_id = cursor.fetchone()[0]
        self.conn.commit()
        return contact_id

    def deleteContactList(self, clist_id):
        cursor = self.conn.cursor()
        query = "delete from contact_list where clist_id = %s;"
        cursor.execute(query, (clist_id,))
        self.conn.commit()
        return clist_id

    def deleteContact(self, contact_id):
        cursor = self.conn.cursor()
        query = "delete from contacts where contact_id = %s;"
        cursor.execute(query, (contact_id,))
        self.conn.commit()
        return contact_id