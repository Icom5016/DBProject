from flask import Flask, request
from handler.messages import MsgHandler
from handler.users import UserHandler
from handler.contactlists import ContactListHandler
from handler.groupChat import GroupChatHandler
from handler.dashboard import DashboardHandler
from handler.hashtag import HashtagHandler
from flask_cors import CORS, cross_origin

#ACTIVATE
app = Flask(__name__)

#Apply CORS to this app
CORS(app)

#################################### INIT ROUTES ####################################

#Home page
@app.route("/MessagingApp")
def home():
    return "Welcome to the social messaging application!"

#Registration page
@app.route("/MessagingApp/register")
def register():
    return "Registration successful"

#Login page
@app.route("/MessagingApp/login")
def login():
    return "Login successful"

#################################### MESSAGE ROUTES ####################################

#Get all the existing messages
@app.route("/MessagingApp/msg", methods=['GET', 'POST'])
def msg():
    if not request.args:
        return MsgHandler().getAllMsg()
    else:
        return MsgHandler.getAllMsg(request.args)

#Get one message using the message id
@app.route("/MessagingApp/msg/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getMsgById(msg_id):
    return MsgHandler().getMsgById(msg_id)

#Get the author (user) of the message
@app.route("/MessagingApp/msg/author/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getAuthorByMsgId(msg_id):
    return MsgHandler().getAuthorByMsgId(msg_id)

#Get the text of a message
@app.route("/MessagingApp/msg/text/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getTextByMsgId(msg_id):
    return MsgHandler().getTextByMsgId(msg_id)

#Get the number of likes of a message
@app.route("/MessagingApp/msg/likes/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getLikesByMsgId(msg_id):
    return MsgHandler().getLikesByMsgId(msg_id)

#get the number of dislikes of a message
@app.route("/MessagingApp/msg/dislikes/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getDislikesByMsgId(msg_id):
    return MsgHandler().getDislikesByMsgId(msg_id)

#get the time of a message
@app.route("/MessagingApp/msg/time/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getTimeByMsgId(msg_id):
    return MsgHandler().getTimeByMsgId(msg_id)

#get the date of a message
@app.route("/MessagingApp/msg/date/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getDateByMsgId(msg_id):
    return MsgHandler().getDateByMsgId(msg_id)

@app.route("/MessagingApp/msg/gchat/<int:gchat_id>", methods=['GET', 'PUT', 'DELETE'])
def getMessagesByChatId(gchat_id):
    return MsgHandler().getMessagesByChatId(gchat_id)

@app.route("/MessagingApp/msg/user/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getAllMsgByUserId(user_id):
    return MsgHandler().getAllMsgByUserId(user_id)

@app.route("/MessagingApp/msg/gchat/user/<int:gchat_id>/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getMessagesByChatIdAndUserId(gchat_id, user_id):
    return MsgHandler().getMessagesByChatIdAndUserId(gchat_id, user_id)

@app.route("/MessagingApp/msg/likes/user/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getAllLikeUsersByMsgID(msg_id):
    return MsgHandler().getAllLikeUsersByMsgID(msg_id)

@app.route("/MessagingApp/msg/dislikes/user/<int:msg_id>", methods=['GET', 'PUT', 'DELETE'])
def getAllDislikeUsersByMsgID(msg_id):
    return MsgHandler().getAllDislikeUsersByMsgID(msg_id)

#Gets the original message using the reply's id
@app.route("/MessagingApp/msg/original/<int:reply_id>", methods=['GET', 'PUT', 'DELETE'])
def getOriginalByReplyId(reply_id):
    return MsgHandler().getOriginalByReplyId(reply_id)

#Gets a list of replies of a message using its id
@app.route("/MessagingApp/msg/reply/<int:original_id>", methods=['GET', 'PUT', 'DELETE'])
def getRepliesByOriginalId(original_id):
    return MsgHandler().getRepliesByOriginalId(original_id)

#Gets a list of all existing messages that are replies
@app.route("/MessagingApp/msg/reply", methods=['GET', 'PUT', 'DELETE'])
def getAllReplies():
    handler = MsgHandler()
    return handler.getAllReplies()

#################################### USER ROUTES ####################################

#Get all existing users
@app.route("/MessagingApp/user", methods=['GET', 'POST'])
def user():
    # if request.method == 'POST':
    #     return UserHandler().insertUser(request.form)
    # else:
        if not request.args:
            return UserHandler().getAllUser()
        else:
            return UserHandler.getAllUser(request.args)

#Get an user using the id
@app.route("/MessagingApp/user/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getUserById(user_id):
    # if request.method == 'GET':
        return UserHandler().getUserById(user_id)
    # elif request.method == 'PUT':
    #     return UserHandler().updateUser(user_id, request.form)
    # elif request.method == 'DELETE':
    #     return UserHandler().deleteUser(user_id)
    # else:
    #     return jsonify(Error="Method not allowed."), 405

#Get an user using the username
@app.route("/MessagingApp/user/<string:username>", methods=['GET', 'PUT', 'DELETE'])
def getUserByUsername(username):
        return UserHandler().getUserByUsername(username)

#Get the first name of an user
@app.route("/MessagingApp/user/fname/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getFNameByUserId(user_id):
    handler = UserHandler()
    return handler.getFNameByUserId(user_id)



#Get the last name of an user
@app.route("/MessagingApp/user/lname/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getLNameByUserId(user_id):
    handler = UserHandler()
    return handler.getLNameByUserId(user_id)

#Get the email of an user
@app.route("/MessagingApp/user/email/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getEmailByUserId(user_id):
    handler = UserHandler()
    return handler.getEmailByUserId(user_id)

#Get the phone of an user
@app.route("/MessagingApp/user/phone/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getPhoneByUserId(user_id):
    handler = UserHandler()
    return handler.getPhoneByUserId(user_id)

# #Get the username of an user
# @app.route("/MessagingApp/user/username/<int:user_id>")
# def getUsernameByUserId(user_id):
#     handler = UserHandler()
#     return handler.getUsernameByUserId(user_id)

#Get the password of an user
@app.route("/MessagingApp/user/password/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getPasswordByUserId(user_id):
    handler = UserHandler()
    return handler.getPasswordByUserId(user_id)

@app.route("/MessagingApp/user/likes/msg/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getLikedMsgByUserId(user_id):
    return UserHandler().getLikedMsgByUserId(user_id)

@app.route("/MessagingApp/user/dislikes/msg/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getDislikedMsgByUserId(user_id):
    return UserHandler().getDislikedMsgByUserId(user_id)

#################################### CONTACT LIST ROUTES  ##################################

#Get all contact lists with their current contacts
@app.route("/MessagingApp/contactlist")
def contactlist():
    # handler = ContactListHandler()
    # return handler.getAllContactList()
    if not request.args:
        return ContactListHandler().getAllContactList()
    else:
        return ContactListHandler.getAllContactList(request.args)

@app.route("/MessagingApp/contactlist/<int:clist_id>", methods=['GET', 'PUT', 'DELETE'])
def getContactListByID(clist_id):
    return ContactListHandler().getContactListByID(clist_id)

#Gets the contact list of a user using the user's id
@app.route("/MessagingApp/contactlist/owner/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getContactListByUserId(user_id):
    handler = ContactListHandler()
    return handler.getContactListByUserId(user_id)

#Not as important
# #Gets some single user that belongs a contact lists
# @app.route("/MessagingApp/contactlist/singlecontact/<int:user_id>")
# def getSingleContactByUserId(user_id):
#     handler = ContactListHandler()
#     return handler.getSingleContactByUserId(user_id)

#################################### (GROUP) CHAT ROUTES  ####################################

#Get all existing group chats
@app.route("/MessagingApp/gchat")
def getAllGroupChats():
    if not request.args:
        return GroupChatHandler().getAllChats()
    else:
        return GroupChatHandler.getAllChats(request.args)

#Get a group chat using its id
@app.route("/MessagingApp/gchat/<int:gchat_id>", methods=['GET', 'PUT', 'DELETE'])
def getGroupChatById(gchat_id):
    return GroupChatHandler().getGroupChatById(gchat_id)

#Get the group chats of an owner (user) using their id
@app.route("/MessagingApp/gchat/owner/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def getAllChatsByOwnerId(user_id):
    return GroupChatHandler().getAllGroupChatByOwnerId(user_id)

#Get a specific group chat using the owner's (user) id and the group chat's name
@app.route("/MessagingApp/gchat/owner/gchat_name/<int:user_id>/<string:gchat_name>", methods=['GET', 'PUT', 'DELETE'])
def getAllChatsByOwnerIdAndChatName(user_id, gchat_name):
    return GroupChatHandler().getGroupChatsByOwnerIdAndName(user_id, gchat_name)

#Gets all chats that have a specific name
@app.route("/MessagingApp/gchat/gchat_name/<string:gchat_name>", methods=['GET', 'PUT', 'DELETE'])
def getAllChatsWithName(gchat_name):
    return GroupChatHandler().getGroupChatsByName(gchat_name)

#Gets all group chats with their respective members
@app.route("/MessagingApp/gchat/members", methods=['GET', 'PUT', 'DELETE'])
def getAllChatsAndMembers():
    handler = GroupChatHandler()
    return handler.getAllChatsAndMembers()

#Gets a group chat and its members using the chat's id
@app.route("/MessagingApp/gchat/members/<int:gchat_id>", methods=['GET', 'PUT', 'DELETE'])
def getChatMembersByChatId(gchat_id):
    handler = GroupChatHandler()
    return handler.getChatMembersByChatID(gchat_id)

#Gets the owner of a gchat
@app.route("/MessagingApp/gchat/getowner/<int:gchat_id>", methods=['GET', 'PUT', 'DELETE'])
def getOwnerOfChat(gchat_id):
    handler = GroupChatHandler()
    return handler.getOwnerOfChat(gchat_id)

#################################### DASHBOARD ROUTES ####################################

#Son aggregates?
# @app.route("/MessagingApp/dashboard")
# def dashboard():
#     handler = DashboardHandler()
#     return handler.getAllDashboard()
#
@app.route("/MessagingApp/dashboard/<string:date>")
def getDashboardByDate(date):
    return DashboardHandler().getDashboardByDate(date)
#
# @app.route("/MessagingApp/dashboard/date/<int:dashboard_id>")
# def getDateByDashboardId(dashboard_id):
#     return DashboardHandler().getDateById(dashboard_id)
#
# @app.route("/MessagingApp/dashboard/<string:date>")
# def getDashboardByDate(date):
#     return DashboardHandler().getDashboardByDate(date)
#

#Get the total messages in a given day
@app.route("/MessagingApp/dashboard/total_messages/<string:date>")
def getTotalMessagesByDate(date):
    return DashboardHandler().getTotalMessagesByDate(date)

#Get the total replies in a given day
@app.route("/MessagingApp/dashboard/total_replies/<string:date>")
def getRepliesByDate(date):
    return DashboardHandler().getRepliesByDate(date)

#Get the total likes in a given day
@app.route("/MessagingApp/dashboard/total_likes/<string:date>")
def getTotalLikesByDate(date):
    return DashboardHandler().getLikesByDate(date)

#Get the total dislikes in a given day
@app.route("/MessagingApp/dashboard/total_dislikes/<string:date>")
def getTotalDislikesByDate(date):
    return DashboardHandler().getDislikesByDate(date)

#Get the total active users in a given day
@app.route("/MessagingApp/dashboard/active_users/<string:date>")
def getActiveUsersByDate(date):
    return DashboardHandler().getActiveUsersByDate(date)

#################################### HASHTAG ROUTES ####################################

#Get all existing hashtags
@app.route("/MessagingApp/hashtag")
def hashtag():
    handler = HashtagHandler()
    return handler.getAllHashtag()

#Get all hashtags in a message using message id
@app.route("/MessagingApp/hashtags/msg/<int:msg_id>")
def getHashtagdByMsgId(msg_id):
    return HashtagHandler().getHashtagByMsgId(msg_id)

#For some reason a text starting with '#' doesn't work

#Get all messages that contain a hashtag using the hashtag text
@app.route("/MessagingApp/msgs/hashtag/<string:hashtag_text>")
def getMsgsByHashtagText(hashtag_text):
    return HashtagHandler().getMsgsByHashtagText(hashtag_text)

# #Get the frequency at wich a hashtag has been used using its id
# @app.route("/MessagingApp/hashtag/frequency/<int:hashtag_id>")
# def getFrequencyByHashtagId(hashtag_id):
#     return HashtagHandler().getFrequencyByHashtagId(hashtag_id)

@app.route("/MessagingApp/hashtag/<int:hashtag_id>")
def getHashtagByID(hashtag_id):
    return HashtagHandler().getHashtagByID(hashtag_id)

#Get the frequency at wich a hashtag has been used using its text
@app.route("/MessagingApp/hashtag/frequency/<string:hashtag_text>")
def getFrequencyByHashtagText(hashtag_text):
    return HashtagHandler().getFrequencyByHashtagText(hashtag_text)

#Get trending hashtags ordered by hashtag text frequency
@app.route("/MessagingApp/trending_hashtags")
def getTrendingHashtag():
    return HashtagHandler().getTrendingHashtag()

#Get trending hashtag in a group chat by hashtag text frequency
@app.route("/MessagingApp/trending_hashtags/gchat/<int:gchat_id>")
def getTrendingHashtagsByGchatId(gchat_id):
    return HashtagHandler().getTrendingHashtagByGchatId(gchat_id)

if __name__ == '__main__':
    app.run()
