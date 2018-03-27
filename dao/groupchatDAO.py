class gcDAO:
    def __init__(self):
        #[groupchatid, groupchatname, groupchatownerid]
        GC1 = [0, 'Class A', 117]
        GC2 = [1, 'WAZUUUUP', 87]
        GC3 = [2, 'random chat', 10]

        self.data = []
        self.data.append(GC1)
        self.data.append(GC2)
        self.data.append(GC3)

    def getAllChats(self):
        return self.data

    def getChatById(self, Id):
        for r in self.data:
            if (Id == r[0]):
                return r
        return None

    def getAllChatsByOwnerId(self, Id):
        total = []
        for r in self.data:
            if (Id == r[2]):
                total.append(r)
        return total

    def getAllChatsByOwnerIdAndName(self, oid, cn):
        total = []
        for r in self.data:
            if (oid == r[2] and cn == r[1]):
                total.append(r)
        return total

    def getAllChatsByName(self, cn):
        total = []
        for r in self.data:
            if (cn == r[1]):
                total.append(r)
        return total