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
        if result == []:
            return None
        return result


    def getGroupChatById(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat where gchat_id = %s;"
        cursor.execute(query, (gchat_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getAllGroupChatsByOwnerId(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getAllChatsByOwnerIdAndName(self, user_id, gchat_name):
        cursor = self.conn.cursor()
        query = "select * from group_chat where person_id = %s and gchat_name = %s;"
        cursor.execute(query, (user_id, gchat_name,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getAllChatsByName(self, gchat_name):
        cursor = self.conn.cursor()
        query = "select * from group_chat where gchat_name = %s;"
        cursor.execute(query, (gchat_name,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getOwnerOfChat(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select person_id from group_chat where gchat_id = %s;"
        cursor.execute(query, (gchat_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getChatsFromUser(self, person_id):
        cursor = self.conn.cursor()
        query = "select gchat_id, gchat_name, G.person_id " \
                "from group_chat as G inner join chat_members as M " \
                "using (gchat_id) where M.person_id = %s;"
        cursor.execute(query, (person_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertGroupChat(self, gchat_name, person__id):
        cursor = self.conn.cursor()
        query = "insert into group_chat(gchat_name, person_id) " \
                "values (%s, %s) returning gchat_id;"
        cursor.execute(query, (gchat_name, person__id,))
        gchat_id = cursor.fetchone()[0]
        self.conn.commit()
        return gchat_id

    def insertMember(self, gchat_id, person__id):
        cursor = self.conn.cursor()
        query = "insert into chat_members(gchat_id, person_id) " \
                "values (%s, %s) returning member_id;"
        cursor.execute(query, (gchat_id, person__id,))
        member_id = cursor.fetchone()[0]
        self.conn.commit()
        return member_id

    def deleteGroupChat(self, gchat_id):
        cursor = self.conn.cursor()
        query = "delete from group_chat where gchat_id = %s;"
        cursor.execute(query, (gchat_id,))
        self.conn.commit()
        return gchat_id

    def deleteMember(self, member_id):
        cursor = self.conn.cursor()
        query = "delete from chat_members where member_id = %s;"
        cursor.execute(query, (member_id,))
        self.conn.commit()
        return member_id