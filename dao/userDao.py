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
        if result == []:
            return None
        return result

    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result


    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from person where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getFNameByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select first_name from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getLNameByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select last_name from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result


    def getEmailByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select email from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getPhoneByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select phone from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getPasswordByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select password from person where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getLikedMsgByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id " \
                "from message as M, react as R " \
                "where M.msg_id = R.msg_id and R.likes = true and R.person_id = %s;"
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getDislikedMsgByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id " \
                "from message as M, react as R " \
                "where M.msg_id = R.msg_id and R.dislikes = true and R.person_id = %s;"
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result