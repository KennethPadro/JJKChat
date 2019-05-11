from flask import jsonify
from dao.user import UserDAO
from dictionaryMapping import *


class UserHandler:

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapUserToDict(r))
        return jsonify(mapped_result)

    def getUserById(self, uID):
        dao = UserDAO()
        result = dao.getUserByID(uID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapUserToDict(result)
        return jsonify(mapped_result)

    def getOwnedGroupByUserID(self, uID):
        dao = UserDAO()
        result = dao.getOwnedGroupByUserID(uID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapGroupToDict(r))
        return jsonify(mapped_result)

    def getContactsbyUserID(self, uID):
        dao = UserDAO()
        result = dao.getContactsByUserID(uID)
        if not result:
            return jsonify(Error="No contacts"), 777
        mapped_result = []
        for r in result:
            mapped_result.append(mapUserToDict(r))
        return jsonify(mapped_result)

    def getToWhatGroupUserIsMember(self, uID):
        dao = UserDAO()
        result = dao.getToWhatGroupUserIsMember(uID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapGroupToDict(r))
        return jsonify(mapped_result)

    def searchUser(self, args):
        first_name = args.get("name")
        email = args.get("email")
        phone = args.get("phone")
        username = args.get("username")
        user_id = args.get("user_id")
        dao = UserDAO()
        result = None
        if email:
            result = dao.getUserByEmail(email)
        elif phone:
            result = dao.getUserByPhone(phone)
        elif first_name:
            result = dao.getUserByFirstName(first_name)
        elif username:
            result = dao.getUserByUsername(username)
        elif user_id:
            result = dao.getUserByID(user_id)

        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapUserToDict(result)

        return jsonify(mapped_result)


    def getMostActiveUser(self):
        dao = UserDAO()
        result = dao.getMostActiveUser()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapMostActiveUserToDict(r))
        return jsonify(mapped_result)

    def loginUser(self, json):
        dao = UserDAO()

        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400

        username = json['username']
        password = json['password']

        if username and password:
            result = dao.loginUser(username, password)

            if not result:
                return jsonify(Error="Error Not Found"), 404

            mapped_result = {}
            mapped_result['user_id'] = result[0]
            mapped_result['authenticated'] = result[1]

            return jsonify(mapped_result)
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def registerUser(self, json):
        dao = UserDAO()

        if len(json) != 6:
            return jsonify(Error="Malformed post request"), 400

        first_name = json['first_name']
        last_name = json['last_name']
        email = json['email']
        phone = json['phone']
        password = json['password']
        username = json['username']

        if username and password and first_name and last_name and phone and email:
            user_id = dao.registerUser(first_name, last_name, email, phone, password, username)
            return jsonify(user_id), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def addUserToContactList(self, uID, json):
        dao = UserDAO()
        if json.get('first_name')==None or json.get('last_name')==None or (json.get('phone')==None and json.get('email')==None):
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = json['first_name']
            lastname = json['last_name']

            if json.get('phone')!="" and json.get('email')!="":
                phone = json['phone']
                email = json['email']
            elif json.get('email')!="":
                email = json['email']
                phone = None
            elif json.get('phone')!="":
                email = None
                phone = json['phone']

            if firstname and lastname and phone and email:
                contact_uID = dao.getUserID1(firstname, lastname, email, phone)
                if contact_uID == None:
                    result = "User does not exist"
                    return jsonify(result), 404
                dao.addContact(uID, contact_uID[0])
                result = "User was added to contactlist"
                return jsonify(result), 201

            elif firstname and lastname and phone:
                contact_uID = dao.getUserID2(firstname, lastname, phone)
                if contact_uID == None:
                    result = "User does not exist"
                    return jsonify(result), 404
                dao.addContact(uID, contact_uID[0])
                result = "User was added to contactlist"
                return jsonify(result), 201

            elif firstname and lastname and email:
                contact_uID = dao.getUserID3(firstname, lastname, email)
                if contact_uID == None:
                    result = "User does not exist"
                    return jsonify(result), 404
                dao.addContact(uID, contact_uID[0])
                print(contact_uID)
                result = "User was added to contactlist"
                return jsonify(result), 201

    def removeContactsbyUserID(self,uID,json):
        dao = UserDAO()
        result = dao.deleteContact(uID, json.get('user_id'))
        return "Contact deleted"