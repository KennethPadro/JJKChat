from flask import Flask, request
from handler.user import UserHandler
from handler.group import GroupHandler
from handler.post import PostHandler
from handler.hashtag import HashtagHandler
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

CORS(app)

@app.route('/')
def home():
    return "Welcome to JJKChat api"

#Register to the application.
@app.route('/JJKChat/register', methods=['POST'])
def registerUser():
    return UserHandler().registerUser(request.json)

#Login an existing user
@app.route('/JJKChat/login', methods=['POST'])
def loginUser():
    return UserHandler().loginUser(request.json)

#Get all users #Search for a user #Register a user
@app.route('/JJKChat/user', methods=['GET'])
def getAllUsers():
    if request.args:
        return UserHandler().searchUser(request.args)
    else:
        return UserHandler().getAllUsers()

#Gets contacts of an user . Add user to contacts
@app.route('/JJKChat/user/<int:uID>/contact', methods=['GET','POST','DELETE'])
def getContactsByUserID(uID):
    if request.method == 'POST':
        return UserHandler().addUserToContactList(uID, request.json)
    if request.method == 'GET':
        return UserHandler().getContactsbyUserID(uID)
    if request.method == 'DELETE':
        return UserHandler().removeContactsbyUserID(uID, request.json)

#Get specific user by ID
@app.route('/JJKChat/user/<int:uID>', methods=['GET'])
def getUserByID(uID):
    return UserHandler().getUserById(uID)

#get what groups the user is owner of
@app.route('/JJKChat/user/<int:uID>/ownedgroups', methods=['GET'])
def getOwnedGroupByUserID(uID):
    return UserHandler().getOwnedGroupByUserID(uID)

#Gets to what groups a users is member of
@app.route('/JJKChat/user/<int:uID>/member', methods=['GET'])
def getMemberOfGroupsByUserID(uID):
    return UserHandler().getToWhatGroupUserIsMember(uID)

#Get all groups Create a chatgroup Delete a Chatgroup
@app.route('/JJKChat/group', methods=['GET','POST','DELETE'])
def getGroup():
    if request.method == 'GET':
        return GroupHandler().getAllGroups()
    if request.method == 'POST':
        return GroupHandler().createGroup(request.json)
    if request.method == 'DELETE':
        return GroupHandler().deleteGroup(request.json)

#Gets members of a group by group ID
@app.route('/JJKChat/group/<int:gID>/members', methods=['POST', 'GET','DELETE'])
def getMembersByGroupID(gID):
    if request.method == 'GET':
        return GroupHandler().getGroupMembersByGroupID(gID)
    if request.method == 'POST':
        return GroupHandler().addMember(gID, request.json)
    if request.method == 'DELETE':
        return GroupHandler().removeMember(gID, request.json)

#Get all posts by group id
@app.route('/JJKChat/group/<int:gID>/post', methods=['GET','POST'])
def getPostByGroupId(gID):
    if request.method == 'GET':
        return PostHandler().getPostByGroupId(gID)
    elif request.method == 'POST':
        return PostHandler().addPost(gID, request)

#Get all posts by group id
@app.route('/JJKChat/group/<int:gID>/detailedpost', methods=['GET'])
def getPostByGroupIdDETAILED(gID):
    if request.method == 'GET':
        return PostHandler().getPostByGroupIdDETAILED(gID)

#Get specific group by ID
@app.route('/JJKChat/group/<int:gID>', methods=['GET'])
def getGroupByID(gID):
    return GroupHandler().getGroupByGroupID(gID)

#Gets specific groups owner by group ID
@app.route('/JJKChat/group/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getGroupOwnerByGroupID(gID)

#Get all posts
@app.route('/JJKChat/post', methods=['GET'])
def getAllPost():
    if request.method == 'GET':
        return PostHandler().getAllPost()

# #Get specific post by Id
# @app.route('/JJKChat/post/<int:pID>', methods=['GET'])
# def getPostByID(pID):
#     return PostHandler().getPostByID(pID)

#Get replies from post by post id
@app.route('/JJKChat/post/<int:pID>/replies', methods=['GET','POST'])
def getRepliesByPostID(pID):
    if request.method == 'POST':
        return PostHandler().replyToPostID(pID, request.json)
    if request.method == 'GET':
        return PostHandler().getRepliesByPostID(pID)

# @app.route('/JJKChat/post/like', methods=['POST'])
# def likeaPost():
#         return PostHandler().reactToPost(request.json, 'like')
#
# @app.route('/JJKChat/post/dislike', methods=['POST'])
# def dislikeaPost():
#         return PostHandler().reactToPost(request.json, 'dislike')

@app.route('/JJKChat/post/<int:pID>/likes', methods=['GET','POST'])
def getListOfUsersWhoLikedPost(pID):
    if request.method == 'GET':
        return PostHandler().getListOfUsersWhoLikedPost(pID)
    if request.method == 'POST':
        return PostHandler().reactToPost(pID, request.json, 'like')

@app.route('/JJKChat/post/<int:pID>/dislikes', methods=['GET','POST'])
def getListOfUsersWhoDislikedPost(pID):
    if request.method == 'GET':
        return PostHandler().getListOfUsersWhoDislikedPost(pID)
    if request.method == 'POST':
        return PostHandler().reactToPost(pID, request.json, 'dislike')

#DELETEEEEEEEEEEEE???
# Statistics 2 Get total number of posts on a certain date
# @app.route('/JJKChat/user/<int:uID>/post/count', methods=['GET'])
# def getNumberOfPostPerDayByUser(uID):
#     return PostHandler().getNumberOfPostPerDayByUser(uID)

# Statistics 3
@app.route('/JJKChat/replies/count', methods=['GET'])
def getNumberOfRepliesPerDay():
    return PostHandler().getNumberOfRepliesPerDay()

# Statistics 4
@app.route('/JJKChat/likes/count', methods=['GET'])
def getNumberOfLikesPerDay():
    return PostHandler().getNumberOfLikesPerDay()

#statistics 5
@app.route('/JJKChat/dislikes/count', methods=['GET'])
def getNumberOfDislikesPerDay():
    return PostHandler().getNumberOfDislikesPerDay()

#Statistics 9
@app.route('/JJKChat/post/<int:pID>/likes/count', methods=['GET'])
def getNumberOfLikesForGivenPost(pID):
    return PostHandler().getNumberOfLikesForGivenPost(pID)

@app.route('/JJKChat/post/<int:pID>/dislikes/count', methods=['GET'])
def getNumberOfDislikesForGivenPost(pID):
    return PostHandler().getNumberOfDislikesForGivenPost(pID)

#Statistics 8
@app.route('/JJKChat/replies/<int:pID>/count', methods=['GET'])
def getNumberOfRepliesForGivenPost(pID):
    return PostHandler().getNumberOfRepliesForGivenPost(pID)

#Statistics 7 Get specific user posts number by user id
@app.route('/JJKChat/user/<int:uID>/postsperday', methods=['GET'])
def getNumberOfPostsPerDayByUser(uID):
    return PostHandler().getNumberOfPostsPerDayByUser(uID)

@app.route('/JJKChat/user/mostactive', methods=['GET'])
def getMostActiveUser():
    return UserHandler().getMostActiveUser()

# Statistics 2 Get total number of posts on a certain date
@app.route('/JJKChat/post/countperday', methods=['GET'])
def getNumberOfPostsPerDay():
    return PostHandler().getNumberOfPostsPerDay()

@app.route('/JJKChat/hashtag/trending', methods=['GET'])
def getTrendingTopic():
    return HashtagHandler().getTrendingHashtag()

if __name__ == '__main__':
    app.run()
