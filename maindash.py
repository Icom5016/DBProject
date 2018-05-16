from flask import Flask, request
from dashhandler.dashhandler import DashHandler
from flask_cors import CORS, cross_origin

#ACTIVATE
app = Flask(__name__)

#Apply CORS to this app
CORS(app)

#RoutesForJsons

#GetLikesOnDate
@app.route("/MessagingApp/dashboard/likes/<string:date>", methods=['GET', 'PUT', 'DELETE'])
def getDashLikesForDate(date):
    return DashHandler().getTotalLikesPerDay(date)

#GetDislikesOnDate
@app.route("/MessagingApp/dashboard/dislikes/<string:date>", methods=['GET', 'PUT', 'DELETE'])
def getDashDislikesForDate(date):
    return DashHandler().getTotalDislikesPerDay(date)

#GetMessagesOnDate
@app.route("/MessagingApp/dashboard/msgs/<string:date>", methods=['GET', 'PUT', 'DELETE'])
def getDashTotMsgsForDate(date):
    return DashHandler().getTotalMessagesPerDay(date)

#GetRepliesOnDate
@app.route("/MessagingApp/dashboard/replies/<string:date>", methods=['GET', 'PUT', 'DELETE'])
def getDashTotRepliesForDate(date):
    return DashHandler().getTotalRepliesPerDay(date)

#Get Top 10 hashtags
@app.route("/MessagingApp/dashboard/trending/<string:date>", methods=['GET', 'PUT', 'DELETE'])
def getOrderedHashtagFrequency(date):
    return DashHandler().getOrderedHashtagFrequency(date)

#GetActiveUsersOnDate
@app.route("/MessagingApp/dashboard/users/<string:date>", methods=['GET', 'PUT', 'DELETE'])
def getActiveUsersForDate(date):
    return DashHandler().getActiveUsersForDate(date)

#Get Top 10 hashtags

#Get Top 10 active users


if __name__ == '__main__':
    app.run()