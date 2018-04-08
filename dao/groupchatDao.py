class GroupChatDAO:
    def __init__(self):
        #[groupchatid, groupchatname, groupchatownerid]
        GC1 = [0, 'Class A', 117]
        GC2 = [1, 'Whats Up!', 87]
        GC3 = [2, 'random chat', 10]

        self.data = []
        self.data.append(GC1)
        self.data.append(GC2)
        self.data.append(GC3)

    def getAllChats(self):
        return self.data

    def getGroupChatById(self, gchat_id):
        for r in self.data:
            if (gchat_id == r[0]):
                return r
        return None

    def getAllGroupChatsByOwnerId(self, user_id):
        total = []
        for r in self.data:
            if (user_id == r[2]):
                total.append(r)
        return total

    def getAllChatsByOwnerIdAndName(self, user_id, gchat_name):
        total = []
        for r in self.data:
            if (user_id == r[2] and gchat_name == r[1]):
                total.append(r)
        return total

    def getAllChatsByName(self, gchat_name):
        total = []
        for r in self.data:
            if (gchat_name == r[1]):
                total.append(r)
        return total

    def getOwnerOfChat(self, gc_id):
        for r in self.data:
            if gc_id == r[0]:
                return r[2]
        return None