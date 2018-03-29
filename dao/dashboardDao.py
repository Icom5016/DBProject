class DashboardDAO:
    def __init__(self):
        #[dashboard id, date, total messages, total replies, total likes, total dislikes, active users]
        D1 = [1, "03/25/2018", 89, 13, 42, 21, 30]
        D2 = [2, "03/26/2018", 15, 2, 3, 1, 6]
        D3 = [3, "03/27/2018", 65, 10, 25, 12, 25]
        D4 = [4, "03/28/2018", 71, 9, 32, 16, 28]

        self.data = []
        self.data.append(D1)
        self.data.append(D2)
        self.data.append(D3)
        self.data.append(D4)

    def getAllDashboard(self):
        return self.data

    def getDashboardById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r
        return None

    def getDashboardByDate(self, date):
        for r in self.data:
            if date == r[1]:
                return r
            return None

    def getDateById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r[1]
        return None

    def getTotalMessagesById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r[2]
        return None

    def getTotalRepliesById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r[3]
        return None

    def getTotalLikesById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r[4]
        return None

    def getTotalDislikesById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r[5]
            return None

    def getActiveUsersById(self, dashboard_id):
        for r in self.data:
            if dashboard_id == r[0]:
                return r[6]
            return None