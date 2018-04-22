from dao2.userDao2 import UserDAO
from dao2.groupchatDao2 import GroupChatDAO
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
        query = "select * from chat_members;"
        cursor.execute(query)

        dao = UserDAO()
        result = []
        chatId = -1
        chat_members = []
        for r in self.data:
            if chatId != r[0]:
                chatId = r[0]
                for r2 in self.data:
                    if chatId == r2[0]:
                        memberId = r2[1]
                        chat_members.append(dao.getUserById(memberId))
                result.append([chatId, chat_members])
                chat_members = []
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

    #
    # cursor = self.conn.cursor()
    # query = "select person_id from chat_members;"
    # cursor.execute(query)
    # result = []
    # for row in cursor:
    #     result.append(row)
    # return result

    # def getChatsByUser(self, user_id):
    #     dao = GroupChatDAO()
    #     result = []
    #     for r in self.data:
    #         if user_id == r[1]:
    #             result.append(dao.getGroupChatById(r[0]))
    #     if not result:
    #         return None
    #     return result
