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

    # def getAllChatsAndMembers(self):
    #     dao = UserDAO()
    #     result = []
    #     chatId = -1
    #     chat_members = []
    #     for r in self.data:
    #         if chatId != r[0]:
    #             chatId = r[0]
    #             for r2 in self.data:
    #                 if chatId == r2[0]:
    #                     memberId = r2[1]
    #                     chat_members.append(dao.getUserById(memberId))
    #             result.append([chatId, chat_members])
    #             chat_members = []
    #     if result == []:
    #         return None
    #     return result
    #
    # cursor = self.conn.cursor()
    # query = "select * from person;"
    # cursor.execute(query)
    # result = []
    # for row in cursor:
    #     result.append(row)
    # return result
    #
    # def getAllChatMembersByChatID(self, gchat_id):
    #     dao = UserDAO()
    #     result = []
    #     chat_members = []
    #     for r in self.data:
    #         if gchat_id == r[0]:
    #             member_id = r[1]
    #             chat_members.append(dao.getUserById(member_id))
    #     result.append(gchat_id)
    #     result.append(chat_members)
    #     if chat_members == []:
    #         return None
    #     return result
    #
    # def getChatsByUser(self, user_id):
    #     dao = GroupChatDAO()
    #     result = []
    #     for r in self.data:
    #         if user_id == r[1]:
    #             result.append(dao.getGroupChatById(r[0]))
    #     if not result:
    #         return None
    #     return result
