from flask import jsonify, request
from dao.DahsboardDao import DashboardDAO

class DashboardHandler():

    # def getAllDashboard(self):
    #     dao = DashboardDAO()
    #     result = dao.getAllDashboard()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToDashboardDict(r))
    #     return jsonify(Dashboard=mapped_result)
    #
    def getDashboardByDate(self, date):
        dao = DashboardDAO()
        result = dao.getDashboardByDate(date)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDashboardDict(result)
            return jsonify(Dashboard=mapped)

    def mapToDashboardDict(self, row):
        result = {}
        result["total_messages"] = row[0]
        result["total_replies"] = row[1]
        result["total_likes"] = row[2]
        result["total_dislikes"] = row[3]
        result["active_users"] = row[4]
        return result
    #
    # def mapToDateDict(self, row):
    #     result = {}
    #     result["date"] = row
    #     return result


    def getTotalMessagesByDate(self, date):
        dao = DashboardDAO()
        result = dao.getTotalMessagesByDate(date)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else :
            return jsonify(Total_Messages=result)

    # def mapToTotalMessagesDict(self, row):
    #     result = {}
    #     result["total_messages"] = row
    #     return result

    def getRepliesByDate(self, date):
        dao = DashboardDAO()
        result = dao.getTotalRepliesByDate(date)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else :
            return jsonify(Total_Replies=result)

    # def mapToRepliesDict(self, row):
    #     result = {}
    #     result["total_replies"] = row
    #     return result

    def getLikesByDate(self, date):
        dao = DashboardDAO()
        result = dao.getTotalLikesByDate(date)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            return jsonify(Total_Likes=result)

    # def mapToLikesDict(self, row):
    #     result = {}
    #     result["total_likes"] = row
    #     return result

    def getDislikesByDate(self, date):
        dao = DashboardDAO()
        result = dao.getTotalDislikesByDate(date)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            return jsonify(Total_Dislikes=result)

    # def mapToDislikesDict(self, row):
    #     result = {}
    #     result["total_dislikes"] = row
    #     return result

    def getActiveUsersByDate(self, date):
        dao = DashboardDAO()
        result = dao.getActiveUsersByDate(date)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            return jsonify(Total_Active_Users=result)

    # def mapToActiveUsersDict(self, row):
    #     result = {}
    #     result["active_users"] = row
    #     return result
    #
    # def getDashboardByDate(self, date):
    #     dao = DashboardDAO()
    #     result = dao.getDashboardByDate(date)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else :
    #         mapped = self.mapToDashboardDict(result)
    #         return jsonify(Dashboard=mapped)
