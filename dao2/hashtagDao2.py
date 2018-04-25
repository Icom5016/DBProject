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
        return result

    def getHashtagById(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select * from Hashtag where hash_id = %s;"
        cursor.execute(query, (hashtag_id,))
        result = cursor.fetchone()
        return result

    def getTextByHashtagId(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select text from Hashtag where hash_id = %s;"
        cursor.execute(query, (hashtag_id,))
        result = cursor.fetchone()
        return result

    def getFrequencyByHashtagId(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select frequency from Hashtag where hash_id = %s;"
        cursor.execute(query, (hashtag_id,))
        result = cursor.fetchone()
        return result

    def getFrequencyByHashtagText(self, text):
        cursor = self.conn.cursor()
        query = "select frequency from Hashtag where text = %s;"
        cursor.execute(query, (text,))
        result = cursor.fetchone()
        return result