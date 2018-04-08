from dao.userDao import UserDAO

class MsgDAO:
    def __init__(self):
        #[msg id, text, likes, dislikes, author id, chat id, time, date]
        M1 = [25, "Hey, guys! Hope you're all well", 2, 0, 117, 3, "02:00", "07/07/2552"]
        M2 = [50, "Yo, John! I'm good. How about you?", 1, 0, 34, 3, "03:00", "07/07/2552"]
        M3 = [75, "You guys are too dumb.", 0, 2, 87, 3, "04:00", "07/07/2552"]
        M4 = [100, "Hello, ma'am", 0, 0, 117, 5, "10:00", "08/22/2552"]
        M5 = [125, "Hello, John", 0, 0, 10, 5, "10:30", "08/22/2552"]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)


    def getAllMsg(self):
        return self.data

    def getMsgById(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                return r
        return None

    def getAuthorByMsgId(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                dao = UserDAO()
                return dao.getUserById(r[4])

    def getTextByMsgID(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                return r[1]
        return None

    def getLikesByMsgID(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                return r[2]
        return None

    def getDislikesByMsgID(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                return r[3]
        return None

    def getTimeByMsgID(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                return r[6]
        return None

    def getDateByMsgID(self, msg_id):
        for r in self.data:
            if msg_id == r[0]:
                return r[7]
        return None

    def getMessagesByChatId(self, gc_id):
        total = []
        for r in self.data:
            if gc_id == r[5]:
                total.append(r)
        return total
