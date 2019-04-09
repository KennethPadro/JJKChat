from flask import Flask, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from handler.user import UserHandler
from handler.group import GroupHandler
from handler.post import PostHandler
from handler.hashtag import HashtagHandler
from flask_cors import CORS, cross_origin
import os

UPLOAD_FOLDER = '/Users/kennethpadro/PycharmProjects/JJKChat/static' #change to get dynamic
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('upload_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/')
def home():
    return "Welcome to JJKChat api"

#Login an existing user
@app.route('/JJKChat/login', methods=['POST'])
def loginUser():
    return UserHandler().loginUser(request.json)

#Get all users #Search for a user #Register a user
@app.route('/JJKChat/user', methods=['GET','POST'])
def getAllUsers():
    if request.method == 'GET':
        if request.args:
            return UserHandler().searchUser(request.args)
        else:
            return UserHandler().getAllUsers()
    if request.method == 'POST':
        return UserHandler().registerUser(request.json)

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

#Get specific user posts by user id
@app.route('/JJKChat/user/<int:uID>/post', methods=['GET'])
def getPostsByUserID(uID):
    return PostHandler().getPostsByUserID(uID)

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
        return PostHandler().addPost(gID,request.json)

#Get all posts by group id
@app.route('/JJKChat/group/<int:gID>/detailedpost', methods=['GET'])
def getPostByGroupIdDETAILED(gID):
    if request.method == 'GET':
        return PostHandler().getPostByGroupIdDETAILED(gID)

@app.route('/JJKChat/group/<int:gID>/post/react', methods=['GET','POST'])
def reactToaPost(gID):
    if request.method == 'GET':
        return PostHandler().getReaction(request.json)
    elif request.method == 'POST':
        return PostHandler().react(gID,request.json)

#Get specific group by ID
@app.route('/JJKChat/group/<int:gID>', methods=['GET'])
def getGroupByID(gID):
    return GroupHandler().getGroupByGroupID(gID)

#Gets specific groups owner by group ID
@app.route('/JJKChat/group/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getGroupOwnerByGroupID(gID)

#Get all posts
@app.route('/JJKChat/post', methods=['GET','POST'])
def getAllPost():
    if request.method == 'GET':
        return PostHandler().getAllPost()

#Get specific post by Id
@app.route('/JJKChat/post/<int:pID>', methods=['GET'])
def getPostByID(pID):
    return PostHandler().getPostByID(pID)

#Get replies from post by post id
@app.route('/JJKChat/post/<int:pID>/replies', methods=['GET'])
def getRepliesByPostID(pID):
    return PostHandler().getRepliesByPostID(pID)

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
#********************METODO TEMPORERO. LA IDEA ES PASARLE EL REACTION COMO PARAMETRO*****************
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

#********************METODO TEMPORERO. LA IDEA ES PASARLE EL REACTION COMO PARAMETRO*****************
@app.route('/JJKChat/post/<int:pID>/likes', methods=['GET'])
def getListOfUsersWhoLikedPost(pID):
    return PostHandler().getListOfUsersWhoLikedPost(pID)

@app.route('/JJKChat/post/<int:pID>/dislikes', methods=['GET'])
def getListOfUsersWhoDislikedPost(pID):
    return PostHandler().getListOfUsersWhoDislikedPost(pID)

# Statistics 2 Get total number of posts on a certain date
@app.route('/JJKChat/post/countperday', methods=['GET'])
def getNumberOfPostsPerDay():
    return PostHandler().getNumberOfPostsPerDay()

@app.route('/JJKChat/hashtag/trending', methods=['GET'])
def getTrendingTopic():
    return HashtagHandler().getTrendingHashtag()

if __name__ == '__main__':
    app.run()
