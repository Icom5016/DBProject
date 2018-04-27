from config.dbconfig import pg_config
import psycopg2

class DashboardDAO():

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getDashboardByDate(self, date):
        result = []
        result.append(self.getTotalMessagesByDate(date))
        result.append(self.getTotalRepliesByDate(date))
        result.append(self.getTotalLikesByDate(date))
        result.append(self.getTotalDislikesByDate(date))
        result.append(self.getActiveUsersByDate(date))
        return result

    def getTotalMessagesByDate(self, date):
        cursor = self.conn.cursor()
        query = "select count(*) from message where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result

    def getTotalRepliesByDate(self, date):
        cursor = self.conn.cursor()
        query = "select count(*) from reply natural inner join message where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result

    def getTotalLikesByDate(self, date):
        cursor = self.conn.cursor()
        query = "select sum(likes) from message where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result

    def getTotalDislikesByDate(self, date):
        cursor = self.conn.cursor()
        query = "select sum(dislikes) from message where date = %s;"
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result

    def getActiveUsersByDate(self, date):
        cursor = self.conn.cursor()
        query = "select count(distinct person_id) from message where date = %s;" #Aqui solo cuenta los users que escriben
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        return result
