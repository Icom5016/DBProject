from dao.userDao import UserDAO

class LikesDAO:
    def __init__(self):
        #[message id, user id, primery key(message id, user id)]

        CM1 = [25, 117, [25, 117]]
        CM2 = [25, 34, [25, 34]]
        CM3 = [25, 87, [25, 87]]
        CM4 = [25, 10, [25, 10]]

        CM5 = [50, 117, [50, 117]]
        CM6 = [50, 10, [50, 10]]

        CM7 = [75, 117, [75, 117]]
        CM8 = [100, 34, [100, 34]]
        CM9 = [125, 87, [125, 87]]

        self.data = []
        self.data.append(CM1)
        self.data.append(CM2)
        self.data.append(CM3)
        self.data.append(CM4)
        self.data.append(CM5)
        self.data.append(CM6)
        self.data.append(CM7)
        self.data.append(CM8)
        self.data.append(CM9)

    def getUsersWhoLikeMessage(self, msg_id):
        total=[]
        for r in self.data:
            if msg_id == r[0]:
                total.append(r[1])
        return total

    def getMessagesLikedByUser(self, u_id):
        total=[]
        for r in self.data:
            if u_id == r[1]:
                total.append(r[0])
        return total