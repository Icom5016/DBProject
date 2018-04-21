from config.dbconfig import pg_config
import psycopg2
class UserDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUser(self):
        cursor = self.conn.cursor()
        query = "select * from person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    ####REMOVED USERNAME ATTRIB
    # def getUserByName(self, username):
    #     for r in self.data:
    #         if username == r[5]:
    #             return r
    #     return None

    def getFNameByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select first_name from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    #
    # def getFNameByName(self, username):
    #     for r in self.data:
    #         if username == r[5]:
    #             return r[1]
    #     return None

    def getLNameByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select last_name from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    # def getLNameByName(self, username):
    #     for r in self.data:
    #         if username == r[5]:
    #             return r[2]
    #     return None

    def getEmailByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select email from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    # def getEmailByName(self, username):
    #     for r in self.data:
    #         if username == r[5]:
    #             return r[3]
    #     return None

    def getPhoneByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select phone from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    # def getPhoneByName(self, username):
    #     for r in self.data:
    #         if username == r[5]:
    #             return r[4]
    #     return None

    # def getUsernameByUserId(self, user_id):
    #     for r in self.data:
    #         if user_id == r[0]:
    #             return r[5]
    #     return None

    def getPasswordByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select password from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result