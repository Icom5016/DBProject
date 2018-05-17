from config.dbconfig import pg_config
import psycopg2

class DashDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    #Get likes in a day
    def getLikesPerDate(self, date):
        cursor = self.conn.cursor()
        query = "select sum(likes) " \
                "from message " \
                "where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    #Get dislikes in a day
    def getDislikesPerDate(self, date):
        cursor = self.conn.cursor()
        query = "select sum(dislikes) " \
                "from message " \
                "where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    #Get number of messages in a day
    def getTotalMessagesPerDate(self, date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from message " \
                "where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    #Get total replies in a day
    def getTotalRepliesPerDate(self, date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from message as M, reply as R " \
                "where M.date = %s and R.msg_id = M.msg_id;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    #Get hashtags ordered in descending config (freq)
    def getOrderedHashtagFrequency(self, date):
        cursor = self.conn.cursor()
        query = "select H.hash_text, count(*) " \
                "from hashtag as H, message as M " \
                "where H.msg_id = M.msg_id " \
                "and M.date = %s " \
                "group by hash_text " \
                "order by count(*) DESC " \
                "limit 10"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    # #Get a list of users and messages sent in a day
    # def getOrderedUserMessageFrequency(self, date):
    #     cursor = self.conn.cursor()
    #     query="select username, count(*) " \
    #           "from message " \
    #           "group by username " \
    #           "order by count* DESC " \
    #           "limit 10;"
    #     cursor.execute(query, (date,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     if result == []:
    #         return None
    #     return result

    #Get number of active users on a day
    def getActiveUsersForDate(self, date):
        cursor = self.conn.cursor()
        query= "select P.username, count(*) as messages " \
               "from person as P, message as M " \
               "where P.person_id = M.person_id " \
               "and M.date = %s " \
               "group by P.username " \
               "order by count(*) DESC " \
               "limit 10"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result