from flask import Flask, request
from handler.messages import MsgHandler
from handler2.users2 import UserHandler
from handler.contactlists import ContactListHandler
from handler.reply import ReplyHandler
from handler2.groupChat2 import GroupChatHandler
from handler.dashboard import DashboardHandler
from handler.hashtag import HashtagHandler

app = Flask(__name__)

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

#################################### MESSAGE ROUTES

#Get all the existing messages
@app.route("/MessagingApp/msg")
def msg():
    handler = MsgHandler()
    return handler.getAllMsg()

#Get one message using the message id
@app.route("/MessagingApp/msg/<int:msg_id>")
def getMsgById(msg_id):
    return MsgHandler().getMsgById(msg_id)

#Get the author (user) of the message
@app.route("/MessagingApp/msg/author/<int:msg_id>")
def getAuthorByMsgId(msg_id):
    return MsgHandler().getAuthorByMsgId(msg_id)

#Get the text of a message
@app.route("/MessagingApp/msg/text/<int:msg_id>")
def getTextByMsgId(msg_id):
    return MsgHandler().getTextByMsgId(msg_id)

#Get the number of likes of a message
@app.route("/MessagingApp/msg/likes/<int:msg_id>")
def getLikesByMsgId(msg_id):
    return MsgHandler().getLikesByMsgId(msg_id)

#get the number of dislikes of a message
@app.route("/MessagingApp/msg/dislikes/<int:msg_id>")
def getDislikesByMsgId(msg_id):
    return MsgHandler().getDislikesByMsgId(msg_id)

#get the time of a message
@app.route("/MessagingApp/msg/time/<int:msg_id>")
def getTimeByMsgId(msg_id):
    return MsgHandler().getTimeByMsgId(msg_id)

#get the date of a message
@app.route("/MessagingApp/msg/date/<int:msg_id>")
def getDateByMsgId(msg_id):
    return MsgHandler().getDateByMsgId(msg_id)

#Gets the original message using the reply's id
@app.route("/MessagingApp/msg/original/<int:reply_id>")
def getOriginalByReplyId(reply_id):
    return ReplyHandler().getOriginalByReplyId(reply_id)

#Gets a list of replies of a message using its id
@app.route("/MessagingApp/msg/reply/<int:original_id>")
def getRepliesByOriginalId(original_id):
    return ReplyHandler().getRepliesByOriginalId(original_id)

#Gets a list of all existing messages that are replies
@app.route("/MessagingApp/msg/reply")
def getAllReplies():
    handler = ReplyHandler()
    return handler.getAllReplies()

#################################### USER ROUTES

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

#################################### CONTACT LIST ROUTES

#Get all contact lists with their current contacts
@app.route("/MessagingApp/contactlist")
def contactlist():
    handler = ContactListHandler()
    return handler.getAllContactList()

#Gets the contact list of a user using the user's id
@app.route("/MessagingApp/contactlist/owner/<int:user_id>")
def getContactListByUserId(user_id):
    handler = ContactListHandler()
    return handler.getContactListByUserId(user_id)

#Gets some single user that belongs a contact lists
@app.route("/MessagingApp/contactlist/singlecontact/<int:user_id>")
def getSingleContactByUserId(user_id):
    handler = ContactListHandler()
    return handler.getSingleContactByUserId(user_id)

#################################### (GROUP) CHAT ROUTES

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

#################################### DASHBOARD ROUTES

@app.route("/MessagingApp/dashboard")
def dashboard():
    handler = DashboardHandler()
    return handler.getAllDashboard()

@app.route("/MessagingApp/dashboard/<int:dashboard_id>")
def getDashboardById(dashboard_id):
    return DashboardHandler().getDashboardById(dashboard_id)

@app.route("/MessagingApp/dashboard/date/<int:dashboard_id>")
def getDateByDashboardId(dashboard_id):
    return DashboardHandler().getDateById(dashboard_id)

@app.route("/MessagingApp/dashboard/<string:date>")
def getDashboardByDate(date):
    return DashboardHandler().getDashboardByDate(date)

@app.route("/MessagingApp/dashboard/total_messages/<int:dashboard_id>")
def getTotalMessagesByDashboardId(dashboard_id):
    return DashboardHandler().getTotalMessagesById(dashboard_id)

@app.route("/MessagingApp/dashboard/total_replies/<int:dashboard_id>")
def getRepliesByDashboardId(dashboard_id):
    return DashboardHandler().getRepliesById(dashboard_id)

@app.route("/MessagingApp/dashboard/total_likes/<int:dashboard_id>")
def getTotalLikesByDashboardId(dashboard_id):
    return DashboardHandler().getLikesById(dashboard_id)

@app.route("/MessagingApp/dashboard/total_dislikes/<int:dashboard_id>")
def getTotalDislikesByDashboardId(dashboard_id):
    return DashboardHandler().getDislikesById(dashboard_id)

@app.route("/MessagingApp/dashboard/active_users/<int:dashboard_id>")
def getActiveUsersByDashboardId(dashboard_id):
    return DashboardHandler().getActiveUsersById(dashboard_id)

#################################### HASHTAG ROUTES

#Get all existing hashtags
@app.route("/MessagingApp/hashtag")
def hashtag():
    handler = HashtagHandler()
    return handler.getAllHashtag()

#Get a hashtag using its id
@app.route("/MessagingApp/hashtag/<int:hashtag_id>")
def getHashtagdById(hashtag_id):
    return HashtagHandler().getHashtagById(hashtag_id)

#Get a hashtag's text using its id
@app.route("/MessagingApp/hashtag/text/<int:hashtag_id>")
def getTextByHashtagId(hashtag_id):
    return HashtagHandler().getTextByHashtagId(hashtag_id)

#Get the frequency at wich a hashtag has been used using its id
@app.route("/MessagingApp/hashtag/frequency/<int:hashtag_id>")
def getFrequencyByHashtagId(hashtag_id):
    return HashtagHandler().getFrequencyByHashtagId(hashtag_id)

#Get the frequency at wich a hashtag has been used using its text
@app.route("/MessagingApp/hashtag/frequency/<string:hashtag_text>")
def getFrequencyByHashtagText(hashtag_text):
    return HashtagHandler().getFrequencyByHashtagText(hashtag_text)

if __name__ == '__main__':
    app.run()