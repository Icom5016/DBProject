from dao2.userDao2 import UserDAO
from config.dbconfig import pg_config
import psycopg2

class MsgDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMsg(self):
        cursor = self.conn.cursor()
        query = "select * from message;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getMsgById(self, msg_id):
        cursor = self.conn.cursor()
        query = "select * from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getAuthorByMsgId(self, msg_id):
        cursor = self.conn.cursor()
        query = "select person_id from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getTextByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select text from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getLikesByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select likes from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getDislikesByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select dislikes from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getTimeByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select time from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getDateByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select date from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getUserMessages(self):
        pass
        # cursor = self.conn.cursor()
        # query = "select person_id, from person;"
        # cursor.execute(query)

    def getUserMessagesByUserId(self, user_id):
        pass

    def getMessagesByChatId(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat as C, message as M where " \
                "C.gchat_id = M.gchat_id and C.gchat_id = %s;"
        cursor.execute(query, (gchat_id,))
        joined_result = []

        for row in cursor:
            joined_result.append(row)

        result = []
        for r in joined_result:
            result.append([r[3], r[4], r[5], r[6], r[7],
                           r[8], r[10], r[1]])
        return result

    def getMessagesByChatIdAndUserId(self, gc_id, user_id):
        # total = []
        # for r in self.data:
        #     if gc_id == r[5] and user_id == r[4]:
        #         total.append(r)
        # if not total:
        #     return None
        # return total
        pass

    def getOriginalByReplyId(self, reply_id):
        for r in self.data:
            if r[1] == reply_id:
                dao = MsgDAO()
                original_id = r[0]
                return dao.getMsgById(original_id)
        return None

    def getRepliesByOriginalId(self, original_id):
        dao = MsgDAO()
        result = []
        for r in self.data:
            if r[0] == original_id:
                reply_id = r[1]
                result.append(dao.getMsgById(reply_id))
        if result == []:
            return None
        return result

    def getAllReplies(self):
        dao = MsgDAO()
        result = []
        for r in self.data:
            result.append(dao.getMsgById(r[1]))
        if result == []:
            return None
        return result