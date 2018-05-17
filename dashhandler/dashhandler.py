from flask import jsonify, request
from dashdao.dashdao import DashDAO

class DashHandler:
    def mapToTotalLikesDict(self, row):
        result = {}
        result["likes"] = row[0]
        return result

    def mapToTotalDislikesDict(self, row):
        result = {}
        result["dislikes"] = row[0]
        return result

    def mapToTotalMsgDict(self, row):
        result = {}
        result["messages"] = row[0]
        return result

    def mapToTotalRepliesDict(self, row):
        result = {}
        result["replies"] = row[0]
        return result

    def mapToTotalActiveUsersDict(self, row):
        result = {}
        result["User"] = row[0]
        result["Messages"] = row[1]
        return result

    def mapToOrderedHashtagFrequencyDict(self, row):
        result = {}
        result["hashtag"] = row[0]
        result["frequency"] = row[1]
        return result

    def getOrderedHashtagFrequency(self, date):
        dao = DashDAO()
        result = dao.getOrderedHashtagFrequency(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToOrderedHashtagFrequencyDict(r))
            return jsonify(Trending=mapped_result)

    def getActiveUsersForDate(self, date):
        dao = DashDAO()
        result = dao.getActiveUsersForDate(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToTotalActiveUsersDict(r))
            return jsonify(Active_Uers=mapped_result)

    def getTotalLikesPerDay(self, date):
        dao = DashDAO()
        result = dao.getLikesPerDate(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTotalLikesDict(result)
            return jsonify(Message=mapped)

    def getTotalDislikesPerDay(self, date):
        dao = DashDAO()
        result = dao.getDislikesPerDate(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTotalDislikesDict(result)
            return jsonify(Message=mapped)

    def getTotalRepliesPerDay(self, date):
        dao = DashDAO()
        result = dao.getTotalRepliesPerDate(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTotalRepliesDict(result)
            return jsonify(Message=mapped)

    def getTotalMessagesPerDay(self, date):
        dao = DashDAO()
        result = dao.getTotalMessagesPerDate(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTotalMsgDict(result)
            return jsonify(Message=mapped)