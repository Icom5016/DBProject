from flask import Flask, request
from dashhandler.dashhandler import DashHandler
from flask_cors import CORS, cross_origin

#ACTIVATE
app = Flask(__name__)

#Apply CORS to this app
CORS(app)

#RoutesForJsons

#GetLikesOnDate
@app.route("/MessagingApp/dashboard/likes/<date: date>", methods=['GET', 'PUT', 'DELETE'])
def getDashLikesForDate(date):
    return DashHandler.getTotalLikesPerDay(date)

#GetDislikesOnDate
@app.route("/MessagingApp/dashboard/dislikes/<date: date>", methods=['GET', 'PUT', 'DELETE'])
def getDashDislikesForDate(date):
    return DashHandler.getTotalDislikesPerDay(date)

#GetMessagesOnDate
@app.route("/MessagingApp/dashboard/msgs/<date: date>", methods=['GET', 'PUT', 'DELETE'])
def getDashTotMsgsForDate(date):
    return DashHandler.getTotalMessagesPerDay(date)

#GetRepliesOnDate
@app.route("/MessagingApp/dashboard/replies/<date: date>", methods=['GET', 'PUT', 'DELETE'])
def getDashTotRepliesForDate(date):
    return DashHandler.getTotalRepliesPerDay(date)

#Get Top 10 hashtags

#Get Top 10 active users