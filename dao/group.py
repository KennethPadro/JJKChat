import psycopg2
from config.dbconfig import pg_config


class GroupDAO:

    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
        self.conn = psycopg2._connect(DATABASE_URL)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select * from chat_groups"
        try:
            cursor.execute(query)
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupOwnerByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name , email, phone, username  from chat_groups natural inner JOIN users where chat_group_id = %s "
        try:
            cursor.execute(query, (gID,))
        except psycopg2.Error as e:
            return
        result = cursor.fetchone()
        return result

    def getGroupMembersByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone,  username from chat_group_members natural inner join users where chat_group_id = %s"
        try:
            cursor.execute(query, (gID,))
        except psycopg2.Error as e:
            return
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "SELECT * FROM chat_groups WHERE chat_group_id = %s"
        try:
            cursor.execute(query, (gID,))
        except psycopg2.Error as e:
            return
        result = cursor.fetchone()
        return result

    def createGroup(self, chat_name, user_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO chat_groups (chat_name, user_id) VALUES(%s, %s) RETURNING chat_group_id"
        cursor.execute(query, (chat_name, user_id, ))
        result = cursor.fetchone()
        self.conn.commit()
        return result[0]

    def deleteGroup(self,chat_group_id, ownerId):
        cursor = self.conn.cursor()
        query = "DELETE FROM chat_groups WHERE chat_group_id = %s AND user_id = %s RETURNING chat_group_id"
        cursor.execute(query, (chat_group_id, ownerId,))
        result = cursor.fetchone()
        self.conn.commit()
        return result[0]

    def addContactTogroup(self, chat_group_id, user_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO chat_group_members VALUES(%s, %s)"
        cursor.execute(query, (user_id, chat_group_id,))
        self.conn.commit()
        return "Contact added to group"

    def removeContactFromGroup(self, chat_group_id, user_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM chat_group_members WHERE chat_group_id= %s AND user_id = %s"  #Verificar esto!!!!!!!!!!!!
        cursor.execute(query, (chat_group_id, user_id))
        self.conn.commit()
        return "chat member removed"