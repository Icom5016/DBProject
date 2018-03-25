from dao.userDao import UserDAO

class MsgDAO:
    def __init__(self):
        #[msg id, text, likes, dislikes, author id, chat id, time-date]
        M1 = [25, "Hey, guys! Hope you're all well", 2, 0, 117, 3, "02:00 - 07/07/2552"]
        M2 = [50, "Yo, John! I'm good. How about you?", 1, 0, 34, 3, "03:00 - 07/07/2552"]
        M3 = [75, "You guys are too dumb.", 0, 2, 87, 3, "04:00 - 07/07/2552"]
        M4 = [100, "Hello, ma'am", 0, 0, 117, 5, "10:00 - 08/22/2552"]
        M5 = [125, "Hello, John", 0, 0, 10, 5, "10:30 - 08/22/2552"]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)


    def getAllMsg(self):
        return self.data

    def getMsgById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getAuthorByMsgId(self, id):
        #With loop
        for r in self.data:
            if id == r[0]:
                dao = UserDAO()
                return dao.getUserById(r[4])
        #Without loop
        # if id == 25:
        #     return ["117", "John"]
        # elif id == 50:
        #     return ["34", "Sam"]
        # elif id == 75:
        #     return ["87", "Kelly"]
        # elif id == 100:
        #     return ["117", "John"]
        # elif id == 125:
        #     return ["10", "Dr. Halsey"]
        # else:
        #     return None

    def getTextByMsgID(self, id):
        # With loop
        for r in self.data:
            if id == r[0]:
                return r[1]
        return None

    def getLikesByMsgID(self, id):
        # With loop
        for r in self.data:
            if id == r[0]:
                return r[2]
        return None

    def getDislikesByMsgID(self, id):
        # With loop
        for r in self.data:
            if id == r[0]:
                return r[3]
        return None

    #En vez de "search sent to" buscamos el chat. In a group chat esto devolveria un list de users, pero
    #ese list ya esta en el table de users que estan en un chat. Creo que getChat tiene mas sentido
    def getChatByMsgID(self, id):
        pass

    def getTimeByMsgID(self, id):
        pass





    #Not sure si estos van. Maybe van en un Dao file dedicato a just replies
    def getRepliesByMsgID(self, id):
        pass

    def getOriginalByMsgID(self, id):
        pass


    #No tienen que ver con un single msg id. Returns a list of msgs
    #Probably belongs in UserDAO file and returns all of the msgs that the user has created
    # def searchByAuthor(self, color):
    #     result = []
    #     for r in self.data:
    #         if color == r[3]:
    #             result.append(r)
    #     return result
