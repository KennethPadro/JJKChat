from dao.data import Data
from config.dbconfig import pg_config
import psycopg2


class UserDAO:

    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
        self.conn = psycopg2._connect(DATABASE_URL)

    users = Data().users
    groups = Data().groups
    contacts = Data().contacts
    posts = Data().posts
    members = Data().group_members

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, username from users;"
        try:
            cursor.execute(query)
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByID(self,uID):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, username from users where user_id = %s;"
        try:
            cursor.execute(query,(uID,))
        except psycopg2.Error as e:
            return
        result = cursor.fetchone()
        return result

    def getUserByUsername(self, uUn):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone, username from users where username = %s;"
        try:
            cursor.execute(query,(uUn,))
        except psycopg2.Error as e:
            return
        result = cursor.fetchone()
        return result

    def getOwnedGroupByUserID(self, uID):
        cursor = self.conn.cursor()
        query ="SELECT * FROM chat_groups WHERE user_id = %s"
        try:
            cursor.execute(query,(uID,))
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactsByUserID(self, uID):
        cursor = self.conn.cursor()
        query = "select contact_user_id, first_name, last_name, email, phone, username from contact INNER JOIN users on contact.contact_user_id = users.user_id where contact.user_id = %s;"
        try:
            cursor.execute(query,(uID,))
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToWhatGroupUserIsMember(self, uID):
        cursor = self.conn.cursor()
        query = "select cg.chat_group_id, cg.chat_name , cg.user_id from chat_groups as cg inner join chat_group_members as cgm on cgm.chat_group_id = cg.chat_group_id where cgm.user_id = %s;"
        try:
            cursor.execute(query,(uID,))
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMostActiveUser(self):
        cursor = self.conn.cursor()
        query = """
                     SELECT user_id, CAST (SUM(r) AS INTEGER)AS interactions
                     FROM(
                     SELECT user_id, count(*) AS r from reactions GROUP BY user_id
                     UNION ALL
                     SELECT user_id, count(*) FROM post GROUP BY user_id
                     UNION ALL
                     SELECT user_id, count(*) AS re FROM reply GROUP BY user_id
                     ) AS queseyo
                     GROUP BY user_id
                     ORDER BY interactions DESC
                     LIMIT 1
                     """
        try:
            cursor.execute(query)
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def loginUser(self, username, password):
        login = "Login Succesfull using " + username + " and " + password
        return login

    def registerUser(self,username, password, firstname, lastname, phone, email):
        return "5"

    def getUserByFirstName(self,uFN):
        user = list(filter(lambda u: u['first_name'] == uFN, self.users))
        return user

    def getUserByLastName(self, uLN):
        user = list(filter(lambda u: u['last_name'] == uLN, self.users))
        return user

    def getUserByPhone(self, uPn):
        user = list(filter(lambda u: u['phone'] == uPn, self.users))
        return user

    def getUserByEmail(self, uEm):
        user = list(filter(lambda u: u['email'] == uEm, self.users))
        return user

    def getReplyByUserID(self,uID):
        posts = list(filter(lambda u: u['user_id'] == uID, self.users))
        return posts

    def addContact(self,uID, firstname, lastname, phone, email):
        return "Done"