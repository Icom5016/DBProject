from dao.userDao import UserDAO
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
        query = "select * from message order by msg_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result


    def getMsgById(self, msg_id):
        cursor = self.conn.cursor()
        query = "select * from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getAuthorByMsgId(self, msg_id):
        cursor = self.conn.cursor()
        query = "select person_id from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getTextByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select text from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getLikesByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select likes from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        if result == []:
            return None
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
        if result == []:
            return None
        return result

    def getDateByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select date from message where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getAllMsgByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from message where person_id = %s  order by msg_id;"
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getMessagesByChatId(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id, M.username " \
                "from group_chat as C, message as M " \
                "where C.gchat_id = M.gchat_id and C.gchat_id = %s " \
                "order by date desc, time desc;"
        cursor.execute(query, (gchat_id,))
        result = []

        for row in cursor:
           result.append(row)
        if result == []:
            return None
        return result

    def getMessagesByChatIdAndUserId(self, gchat_id, user_id):
        cursor = self.conn.cursor()
        query = "select * from message where gchat_id = %s and person_id = %s order by msg_id;"
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
        if result == []:
            return None
        return result

    def getRepliesByOriginalId(self, original_id):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id, M.username " \
                "from message as M, reply as R where M.msg_id = R.msg_id " \
                "and R.original_id = %s order by msg_id"
        cursor.execute(query, (original_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getAllReplies(self):
        cursor = self.conn.cursor()
        query = "select M.msg_id, M.text, M.likes, M.dislikes, M.date, M.time, M.person_id, M.gchat_id, M.username " \
                "from message as M, reply as R where M.msg_id = R.msg_id order by msg_id"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getAllLikeUsersByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select P.person_id, P.first_name, P.last_name, P.email, P.phone, P.password, P.username " \
                "from person as P, react as R " \
                "where P.person_id = R.person_id and R.likes = true and R.msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getAllDislikeUsersByMsgID(self, msg_id):
        cursor = self.conn.cursor()
        query = "select P.person_id, P.first_name, P.last_name, P.email, P.phone, P.password, P.username " \
                "from person as P, react as R " \
                "where P.person_id = R.person_id and R.dislikes = true and R.msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getReactByMsgAndUserID(self, msg_id, person_id):
        cursor = self.conn.cursor()
        query = "select * from react where msg_id = %s and person_id = %s;"
        cursor.execute(query, (msg_id, person_id,))
        result = cursor.fetchone()
        if result == []:
            print("yizus craist")
            return None
        return result

    def insertMsg(self, text, likes, dislikes, person_id, gchat_id, username):
        cursor = self.conn.cursor()
        query = "insert into message(text, likes, dislikes, date, time, person_id, gchat_id, username) " \
                "values (%s, %s, %s, current_date, current_time, %s, %s, %s) returning *;"
        cursor.execute(query, (text, likes, dislikes, person_id, gchat_id, username,))
        msg = cursor.fetchone()
        self.conn.commit()
        return msg

    def insertReply(self, original_id, msg_id):
        cursor = self.conn.cursor()
        query = "insert into reply(original_id, msg_id) " \
                "values (%s, %s) returning reply_id;"
        cursor.execute(query, (original_id, msg_id,))
        reply_id = cursor.fetchone()[0]
        self.conn.commit()
        return reply_id

    def deleteMsg(self, msg_id):
        cursor = self.conn.cursor()
        query = "delete from message where m_id = %s;"
        cursor.execute(query, (msg_id,))
        self.conn.commit()
        return msg_id

    def deleteReply(self, reply_id):
        cursor = self.conn.cursor()
        query = "delete from reply where reply_id = %s returning msg_id;"
        cursor.execute(query, (reply_id,))
        self.conn.commit()
        return reply_id

    def insertReact(self, likes, dislikes, person_id, msg_id):
        cursor = self.conn.cursor()
        query = "insert into react(likes, dislikes, person_id, msg_id) " \
                "values (%s, %s, %s, %s) returning react_id;"
        cursor.execute(query, (likes, dislikes, person_id, msg_id,))
        react_id = cursor.fetchone()[0]
        self.conn.commit()
        return react_id

    def updateReact(self, likes, dislikes, person_id, msg_id):
        cursor = self.conn.cursor()
        query = "update react set likes = %s, dislikes = %s " \
                "where person_id = %s and msg_id = %s " \
                "returning react_id;"
        cursor.execute(query, (likes, dislikes, person_id, msg_id,))
        react_id = cursor.fetchone()[0]
        self.conn.commit()
        return react_id

    def updateReactCount(self, likes, dislikes, msg_id):
        cursor = self.conn.cursor()
        query = "update message set likes = likes + %s, dislikes = dislikes + %s where msg_id = %s"
        cursor.execute(query, (likes, dislikes, msg_id,))
        self.conn.commit()
        return msg_id
