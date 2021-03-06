from config.dbconfig import pg_config
import psycopg2

class HashtagDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHashtag(self):
        cursor = self.conn.cursor()
        query = "select * from Hashtag;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        if not result:
            return None
        return result

    def getAllDistinctHashtag(self):
        cursor = self.conn.cursor()
        query = "select distinct hash_text from Hashtag;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        if not result:
            return None
        return result

    def getHashtagByID(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select hash_id, hash_text " \
                "from hashtag " \
                "where hash_id = %s;"
        cursor.execute(query, (hashtag_id,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getHashtagByMsgId(self, msg_id):
        cursor = self.conn.cursor()
        query = "select hash_id, hash_text from Hashtag where msg_id = %s;"
        cursor.execute(query, (msg_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getMsgsByHashtagText(self, hashtag_text):
        cursor = self.conn.cursor()
        query = "select * from Hashtag natural inner join message where hash_text = %s;"
        cursor.execute(query, (hashtag_text,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getMsgsByChatIdAndHashtagText(self, gchat_id, hashtag_text):
        cursor = self.conn.cursor()
        query = "select * from Hashtag natural inner join message where gchat_id = %s and hash_text = %s;"
        cursor.execute(query, (gchat_id, hashtag_text,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getFrequencyByHashtagText(self, text):
        cursor = self.conn.cursor()
        query = "select hash_text, count(*) from Hashtag where hash_text = %s group by hash_text;"
        cursor.execute(query, (text,))
        result = cursor.fetchone()
        if result == []:
            return None
        return result

    def getTrendingHashtag(self):
        cursor = self.conn.cursor()
        query = "select hash_text, count(*) from hashtag  natural inner join message where " \
                "date = current_date group by hash_text order by count(*) desc limit 10"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def getTrendingHashtagByGchatId(self, gchat_id):
        cursor = self.conn.cursor()
        query = "select hash_text, count(*) from hashtag natural inner join message where " \
                "gchat_id = %s group by hash_text order by count(*) desc"
        cursor.execute(query, (gchat_id,))
        result = []
        for row in cursor:
            result.append(row)
        if result == []:
            return None
        return result

    def insertHashtag(self, hash_text, msg_id):
        cursor = self.conn.cursor()
        query = "insert into hashtag(hash_text, msg_id) " \
                "values (%s, %s) returning hash_id;"
        cursor.execute(query, (hash_text, msg_id,))
        hash_id = cursor.fetchone()[0]
        self.conn.commit()
        return hash_text