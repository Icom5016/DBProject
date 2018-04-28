from dao.userDao import UserDAO
from config.dbconfig import pg_config
import psycopg2

class ChatMembersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllChatsAndMembers(self):
        cursor = self.conn.cursor()
        query = "select C.gchat_id, C.gchat_name, P.person_id " \
                "from group_chat as C, chat_members as M, person as P " \
                "where C.gchat_id = M.gchat_id " \
                "and P.person_id = M.person_id;"
        cursor.execute(query)
        dao = UserDAO()
        result = []
        gchat_id = 0
        members = []

        #Save the data of the cursor to be able to iterate through it multiple times later
        cursor_result = []
        for row in cursor:
            cursor_result.append(row)

        for row in cursor_result:
            if gchat_id != row[0]:
                gchat_id = row[0]
                chat_name = row[1]
                for row2 in cursor_result:
                    if chat_name == row2[1]:
                        person_id = row2[2]
                        members.append(dao.getUserById(person_id))
                result.append([gchat_id, chat_name, members])
                members = []
        if result == []:
            return None
        return result


    def getAllChatMembersByChatID(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select * from chat_members;"
        cursor.execute(query)

        dao = UserDAO()
        result = []
        for row in cursor:
            if row[1] == gchat_id:
                result.append(dao.getUserById(row[2]))
        if result == []:
            return None
        return result

