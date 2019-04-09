from flask import jsonify
from dao.post import PostDAO
from dictionaryMapping import *
from dao.hashtag import HashtagDAO


class PostHandler:

    def getAllPost(self):
        dao = PostDAO()
        result = dao.getAllPosts()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapPostToDict(r))
        return jsonify(mapped_result)

    def getPostByGroupId(self, gID):
        dao = PostDAO()
        result = dao.getPostsByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapPostToDict(r))
        return jsonify(mapped_result)


    def getPostByGroupIdDETAILED(self,gID):
        dao = PostDAO()
        result = dao.getPostsByGroupID(gID)
        mapped_result = []
        for r in result:
            mapped_result.append(mapPostToDictDETAILED(r, self.getRepliesByPostIDDETAILED(r[0])))
        return jsonify(mapped_result)

    def getNumberOfLikesForGivenPost(self, pID):
        dao = PostDAO()
        result = dao.getNumberOfReactionsForGivenPost(pID, "like")
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapReacCountToDict(result)
        return jsonify(mapped_result)

    def getNumberOfDislikesForGivenPost(self, pID):
        dao = PostDAO()
        result = dao.getNumberOfReactionsForGivenPost(pID, "dislike")
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapReacCountToDict(result)
        return jsonify(mapped_result)

    def getListOfUsersWhoLikedPost(self, pID):
        dao = PostDAO()
        result = dao.getListOfUsersWhoReactedPost(pID, "like")
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapToReactDict(r))
        return jsonify(mapped_result)

    def getListOfUsersWhoDislikedPost(self, pID):
        dao = PostDAO()
        result = dao.getListOfUsersWhoReactedPost(pID, "dislike")
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapToReactDict(r))
        return jsonify(mapped_result)

    def getNumberOfPostsPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfPostsPerDay()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapInteractionPerDayToDict(r))
        return jsonify(mapped_result)

    def getNumberOfRepliesPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfRepliesPerDay()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapInteractionPerDayToDict(r))
        return jsonify(mapped_result)

    def getNumberOfLikesPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfLikesPerDay()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapInteractionPerDayToDict(r))
        return jsonify(mapped_result)

    def getNumberOfDislikesPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfDislikesPerDay()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapInteractionPerDayToDict(r))
        return jsonify(mapped_result)

    def getNumberOfRepliesForGivenPost(self, pID):
        dao = PostDAO()
        result = dao.getNumberOfRepliesForGivenPost(pID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapReplyCountToDict(r))
        return jsonify(mapped_result)

    def getNumberOfPostsPerDayByUser(self, uID):
        dao = PostDAO()
        result = dao.getNumberOfPostsPerDayByUser(uID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapInteractionPerDayToDict(result)
        return jsonify(mapped_result)

    def getRepliesByPostID(self, pID):
        dao = PostDAO()
        result = dao.getRepliesByPostID(pID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapReplyToDict(r))
        return jsonify(mapped_result)

    def getRepliesByPostIDDETAILED(self, pID):
        dao = PostDAO()
        result = dao.getRepliesByPostID(pID)
        mapped_result = []
        for r in result:
            mapped_result.append(mapReplyToDict(r))
        return mapped_result

    def getPostByID(self, pID):
        dao = PostDAO()
        result = dao.getPostByID(pID)
        return jsonify(Post=result)

    def getMessageByPostID(self, pID):
        dao = PostDAO()
        result = dao.getMessageByPostID(pID)
        return jsonify(Message=result)

    def getMediaByPostID(self,pID):
        dao = PostDAO()
        result = dao.getMediaByPostID(pID)
        return jsonify(Contacts = result)

    def getAuthorByPostID(self,pID):
        dao = PostDAO()
        result = dao.getAuthorByPostID(pID)
        return jsonify(Author = result)

    def getPostsByUserID(self,uID):
        dao = PostDAO()
        result = dao.getPostsByUserID(uID)
        return jsonify(Post = result)

    def addPost(self,gID, json):
        dao = PostDAO()
        hdao = HashtagDAO
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            groupID = json['groupID']
            author = json['author']
            message = json['message']
            media = json['media']

            if groupID and author and message and media:
                gID = dao.addPost(groupID, author,message, media)

                return jsonify(gID), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def react(self, gID, json):
        return "You reacted to this post"

    def getReaction(self, json):
        return"55 likes"
