class DislikesDAO:
    def __init__(self):
        #[message id, user id, primery key(message id, user id)]

        CM1 = [50, 34, [50, 34]]
        CM2 = [50, 10, [50, 10]]

        CM3 = [75, 10, [75, 10]]

        CM4 = [100, 117, [100, 117]]
        CM5 = [100, 10, [100, 10]]

        self.data = []
        self.data.append(CM1)
        self.data.append(CM2)
        self.data.append(CM3)
        self.data.append(CM4)
        self.data.append(CM5)

    def getUsersWhoDislikeMessage(self, msg_id):
        total=[]
        for r in self.data:
            if msg_id == r[0]:
                total.append(r[1])
        return total

    def getMessagesDislikedByUser(self, u_id):
        total=[]
        for r in self.data:
            if u_id == r[1]:
                total.append(r[0])
        return total
