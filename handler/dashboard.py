from flask import jsonify, request
from dao.dashboardDao import DashboardDAO

class DashboardHandler:
    def getAllDashboard(self):
        dao = DashboardDAO()
        result = dao.getAllDashboard()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDashboardDict(r))
        return jsonify(Dashboard=mapped_result)

    def getDashboardById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getDashboardById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDashboardDict(result)
            return jsonify(Dashboard=mapped)

    def mapToDashboardDict(self, row):
        result = {}
        result["dashboard_id"] = row[0]
        result["date"] = row[1]
        result["total_messages"] = row[2]
        result["total_replies"] = row[3]
        result["total_likes"] = row[4]
        result["total_dislikes"] = row[5]
        result["active_users"] = row[6]
        return result

    def getDateById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getDateById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDateDict(result)
            return jsonify(Dashboard=mapped)

    def mapToDateDict(self, row):
        result = {}
        result["date"] = row
        return result

    def getTotalMessagesById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getTotalMessagesById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTotalMessagesDict(result)
            return jsonify(Dashboard=mapped)

    def mapToTotalMessagesDict(self, row):
        result = {}
        result["total_messages"] = row
        return result

    def getRepliesById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getTotalRepliesById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToRepliesDict(result)
            return jsonify(Dashboard=mapped)

    def mapToRepliesDict(self, row):
        result = {}
        result["total_replies"] = row
        return result

    def getLikesById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getTotalLikesById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToLikesDict(result)
            return jsonify(Dashboard=mapped)

    def mapToLikesDict(self, row):
        result = {}
        result["total_likes"] = row
        return result

    def getDislikesById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getTotalDislikesById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDislikesDict(result)
            return jsonify(Dashboard=mapped)

    def mapToDislikesDict(self, row):
        result = {}
        result["total_dislikes"] = row
        return result

    def getActiveUsersById(self, dashboard_id):
        dao = DashboardDAO()
        result = dao.getActiveUsersById(dashboard_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToActiveUsersDict(result)
            return jsonify(Dashboard=mapped)

    def mapToActiveUsersDict(self, row):
        result = {}
        result["active_users"] = row
        return result

    def getDashboardByDate(self, date):
        dao = DashboardDAO()
        result = dao.getDashboardByDate(date)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDashboardDict(result)
            return jsonify(Dashboard=mapped)
