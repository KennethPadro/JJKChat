import psycopg2
from config.dbconfig import pg_config


class HashtagDAO:

    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
        self.conn = psycopg2._connect(DATABASE_URL)

    def getTrendingHashtag(self):
        cursor = self.conn.cursor()
        query = "SELECT hashtag, ROW_NUMBER ( )  OVER(ORDER BY count(*) DESC) AS position FROM hashtags GROUP BY hashtag LIMIT 10"
        try:
            cursor.execute(query)
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result
