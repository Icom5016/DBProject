from flask import Flask, request
#los py files del handler folder
from handler.messages import MsgHandler
from handler.users import UserHandler

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

if __name__ == '__main__':
    app.run()
