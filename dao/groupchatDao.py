from config.dbconfig import pg_config
import psycopg2

class GroupChatDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllChats(self):
        cursor = self.conn.cursor()
        query = "select * from group_chat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getGroupChatById(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat where gchat_id = %s;"
        cursor.execute(query, (gchat_id,))
        result = cursor.fetchone()
        return result

    def getAllGroupChatsByOwnerId(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result

    #not sure if the way this reads queries is right

    def getAllChatsByOwnerIdAndName(self, user_id, gchat_name):
        cursor = self.conn.cursor()
        query = "select * from group_chat where person_id = %s and gchat_name = %s;"
        cursor.execute(query, (user_id, gchat_name,))
        result = cursor.fetchone()
        return result

    def getAllChatsByName(self, gchat_name):
        cursor = self.conn.cursor()
        query = "select * from group_chat where gchat_name = %s;"
        cursor.execute(query, (gchat_name,))
        result = cursor.fetchone()
        return result

    def getOwnerOfChat(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select person_id from group_chat where gchat_id = %s;"
        cursor.execute(query, (gchat_id,))
        result = cursor.fetchone()
        return result