from dao.data import Data
import psycopg2
from config.dbconfig import pg_config


class HashtagDAO:

    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
        self.conn = psycopg2._connect(DATABASE_URL)

    hashtags = Data().hashtags

    def getAllHashtags(self):
        return self.hashtags

    def getHashtagsByID(self, hID):
        hashtag = list(filter(lambda u: u['hashtag_id'] == hID, self.hashtags))
        return hashtag

    def getHashtagByPostId(self, pID):
        hashtag = list(filter(lambda u: u['post_id'] == pID, self.hashtags))
        return hashtag

    def getTrendingHashtag(self):
        cursor = self.conn.cursor()
        query = "SELECT hashtag, ROW_NUMBER ( )  OVER(ORDER BY count(*) DESC) AS position FROM hashtags GROUP BY hashtag"
        try:
            cursor.execute(query)
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result