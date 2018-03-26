from dao.messageDao import MsgDAO

class ReplyDAO:
    def __init__(self):
        #[original id, reply id, primary key(original, reply)]
        R1 = [25, 50, [25, 50]]
        R2 = [25, 75, [25, 75]]
        R3 = [100, 125, [100, 125]]

        self.data = []
        self.data.append(R1)
        self.data.append(R2)
        self.data.append(R3)

    def getOriginalByReplyId(self, reply_id):
        for r in self.data:
            if r[1] == reply_id:
                dao = MsgDAO()
                original_id = r[0]
                return dao.getMsgById(original_id)
        return None




     def getAllReplies(self):
        pass

    def getRepliesByOriginalId(self, original_id):
        pass