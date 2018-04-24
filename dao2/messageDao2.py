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

    #Not sure what I was going for here
    # def getUserMessages(self):
    #     pass
    #     # cursor = self.conn.cursor()
    #     # query = "select person_id, from person;"
    #     # cursor.execute(query)

    def getAllMsgByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from message where person_id = %s;"
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

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

    def getMessagesByChatIdAndUserId(self, gchat_id, user_id):
        cursor = self.conn.cursor()
        query = "select * from message where gchat_id = %s and person_id = %s;"
        cursor.execute(query, (gchat_id, user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOriginalByReplyId(self, msg_id):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id " \
                "from message as M, reply as R " \
                "where M.msg_id = R.original_id " \
                "and R.msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        return result

    def getRepliesByOriginalId(self, original_id):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id " \
                "from message as M, reply as R where M.msg_id = R.msg_id " \
                "and R.original_id = %s;"
        cursor.execute(query, (original_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReplies(self):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id " \
                "from message as M, reply as R where M.msg_id = R.msg_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllLikeUsersByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select P.person_id, P.first_name, P.last_name, P.email, P.phone, P.password " \
                "from person as P, react as R " \
                "where P.person_id = R.person_id and R.likes = true and R.msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllDislikeUsersByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select P.person_id, P.first_name, P.last_name, P.email, P.phone, P.password " \
                "from person as P, react as R " \
                "where P.person_id = R.person_id and R.dislikes = true and R.msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result