from flask import Flask, request
#los py files del handler folder
from handler.messages import MsgHandler
from handler.users import UserHandler
from handler.contactlists import ContactListHandler
from handler.reply import ReplyHandler
from handler.groupchat import groupchatHandler
from handler.dashboard import DashboardHandler
from handler.hashtag import HashtagHandler


app = Flask(__name__)


@app.route("/MessagingApp")
def home():
    return "Welcome to the social messaging application!"

@app.route("/MessagingApp/login")
def login():
    return "Login successful"

#get all of the messages
@app.route("/MessagingApp/msg")
def msg():
    handler = MsgHandler()
    return handler.getAllMsg()

@app.route("/MessagingApp/msg/<int:msg_id>")
def getMsgById(msg_id):
    return MsgHandler().getMsgById(msg_id)

#@app.route("/MessagingApp/msg/author/")
#Get all auhors... doesn't make much sense anyway so I'll leave it empty for now

@app.route("/MessagingApp/msg/author/<int:msg_id>")
def getAuthorByMsgId(msg_id):
    return MsgHandler().getAuthorByMsgId(msg_id)

@app.route("/MessagingApp/msg/text/<int:msg_id>")
def getTextByMsgId(msg_id):
    return MsgHandler().getTextByMsgId(msg_id)

@app.route("/MessagingApp/msg/likes/<int:msg_id>")
def getLikesByMsgId(msg_id):
    return MsgHandler().getLikesByMsgId(msg_id)

@app.route("/MessagingApp/msg/dislikes/<int:msg_id>")
def getDislikesByMsgId(msg_id):
    return MsgHandler().getDislikesByMsgId(msg_id)

@app.route("/MessagingApp/msg/time/<int:msg_id>")
def getTimeByMsgId(msg_id):
    return MsgHandler().getTimeByMsgId(msg_id)

#get all of the users
@app.route("/MessagingApp/user")
def user():
    handler = UserHandler()
    return handler.getAllUser()

@app.route("/MessagingApp/user/<int:id>")
def getUserById(id):
    return UserHandler().getUserById(id)

@app.route("/MessagingApp/user/fname/<int:id>")
def getFNameByUserId(id):
    print("DEBUG - main")
    handler = UserHandler()
    return handler.getFNameByUserId(id) #Doesn't work with UserHandler().getFNameByUserId(id) for some reason...

@app.route("/MessagingApp/user/lname/<int:id>")
def getLNameByUserId(id):
    handler = UserHandler()
    return handler.getLNameByUserId(id)

@app.route("/MessagingApp/user/email/<int:id>")
def getEmailByUserId(id):
    handler = UserHandler()
    return handler.getEmailByUserId(id)

@app.route("/MessagingApp/user/phone/<int:id>")
def getPhoneByUserId(id):
    handler = UserHandler()
    return handler.getPhoneByUserId(id)

#get all of the messages
@app.route("/MessagingApp/contactlist")
def contactlist():
    handler = ContactListHandler()
    return handler.getAllContactList()

@app.route("/MessagingApp/contactlist/owner/<int:id>")
def getContactListByUserId(id):
    handler = ContactListHandler()
    return handler.getContactListByUserId(id)

@app.route("/MessagingApp/contactlist/singlecontact/<int:id>")
def getSingleContactByUserId(id):
    handler = ContactListHandler()
    return handler.getSingleContactByUserId(id)

@app.route("/MessagingApp/reply/original/<int:reply_id>")
def getOriginalByReplyId(reply_id):
    return ReplyHandler().getOriginalByReplyId(reply_id)

@app.route("/MessagingApp/reply/replies/<int:original_id>")
def getRepliesByOriginalId(original_id):
    return ReplyHandler().getRepliesByOriginalId(original_id)

@app.route("/MessagingApp/reply/")
def getAllReplies():
    return ReplyHandler().getAllReplies()

###################################################################
#####                  GroupChat Entity Routes                #####
###################################################################

@app.route("/MessagingApp/gc")
def getAllGroupChats():
    return groupchatHandler().getAllChats()

@app.route("/MessagingApp/gc/<int:gcid>")
def gettAllChatsById(gcid):
    return groupchatHandler().getGroupChatById(gcid)

@app.route("/MessagingApp/gc/owner/<int:oid>")
def getAllChatsByOwnerId(oid):
    return groupchatHandler().getGroupChatByOwnerId(oid)

@app.route("/MessagingApp/gc/owner/chatname/<int:oid>/<string:name>")
def getAllChatsByOwnerIdAndChatName(oid, name):
    return groupchatHandler().getGroupChatsByOwnerIdAndName(oid, name)

@app.route("/MessagingApp/gc/gcname/<string:name>")
def getAllChatsWithName(name):
    return groupchatHandler().getGroupChatsByName(name)

#Dashboard routes
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

#Hashtag routes
@app.route("/MessagingApp/hashtag")
def hashtag():
    handler = HashtagHandler()
    return handler.getAllHashtag()

@app.route("/MessagingApp/hashtag/<int:hashtag_id>")
def getHashtagdById(hashtag_id):
    return HashtagHandler().getHashtagById(hashtag_id)

@app.route("/MessagingApp/hashtag/text/<int:hashtag_id>")
def getTextByHashtagId(hashtag_id):
    return HashtagHandler().getTextByHashtagId(hashtag_id)

@app.route("/MessagingApp/hashtag/frequency/<int:hashtag_id>")
def getFrequencyByHashtagId(hashtag_id):
    return HashtagHandler().getFrequencyByHashtagId(hashtag_id)

@app.route("/MessagingApp/hashtag/frequency/<string:hashtag_text>")
def getFrequencyByHashtagText(hashtag_text):
    return HashtagHandler().getFrequencyByHashtagText(hashtag_text)

if __name__ == '__main__':
    app.run()
