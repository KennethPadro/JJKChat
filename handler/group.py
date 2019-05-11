from flask import jsonify
from dao.group import GroupDAO
from dictionaryMapping import *


class GroupHandler:

    def getAllGroups(self):
        dao = GroupDAO()
        result = dao.getAllGroups()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapGroupToDict(r))
        return jsonify(mapped_result)

    def getGroupOwnerByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupOwnerByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapUserToDict(result)
        return jsonify(mapped_result)

    def getGroupMembersByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupMembersByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapUserToDict(r))
        return jsonify(mapped_result)

    def getGroupByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapGroupToDict(result)
        return jsonify(mapped_result)

    def createGroup(self, json):
        dao = GroupDAO()
        chat_name = json['chat_name']
        user_id = json['user_id']
        chat_group_id = dao.createGroup(chat_name, user_id)
        dao.addContactTogroup(chat_group_id, user_id) #add user to group
        return jsonify(chat_group_id), 201


    def deleteGroup(self, json):
        dao = GroupDAO()
        chat_group_id = json['chat_group_id']
        user_id = json['user_id']
        result = dao.deleteGroup(chat_group_id, user_id)
        return jsonify(result), 201


    def addMember(self, chat_group_id, json):
        dao = GroupDAO()
        user_id = json['user_id']
        if user_id:
            result = dao.addContactTogroup(chat_group_id, user_id)
            return jsonify(result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def removeMember(self, chat_group_id, json):
        dao = GroupDAO()
        user_id = json['user_id']
        if user_id:
            result = dao.removeContactFromGroup(chat_group_id, user_id)
            return jsonify(result), 200
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400