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
            return jsonify(Error="Not found"), 404
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
        if json is None:
            return jsonify(Error="Malformed post request"), 400

        username = json['username']
        password = json['password']

        if username and password:
            result = dao.loginUser(username,password)
            return jsonify(result)

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def registerUser(self, json):
        dao = UserDAO()
        if len(json) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            username = json['username']
            password = json['password']
            firstname = json['firstname']
            lastname = json['lastname']
            phone = json['phone']
            email = json['email']
            if username and password and firstname and lastname and phone and email:
                uID = dao.registerUser(username, password, firstname, lastname, phone, email)
                result = "User created with id " + uID
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def addUserToContactList(self, uID, json):
        dao = UserDAO()
        if json.get('firstname')==None or json.get('lastname')==None\
                or not(json.get('phone')==None or json.get('email')==None):
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = json['firstname']
            lastname = json['lastname']

            if json.get('phone')!=None:
                phone = json['phone']
                email = None
            elif json.get('email')!=None:
                email = json['email']
                phone = None
            else:
                phone = email = None

            if firstname and lastname and phone:
                uID = dao.addContact(uID, firstname, lastname, phone, None)
                result = "User was added to contactlist"
                return jsonify(result), 201
            elif firstname and lastname and email:
                uID = dao.addContact(uID, firstname, lastname, None, email)
                result = "User was added to contactlist"
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeContactsbyUserID(self,uID,json):
        return "Contact removed"