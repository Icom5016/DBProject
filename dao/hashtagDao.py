class HashtagDAO:
    def __init__(self):
        #[hashtag id, text, frequency]
        H1 = [123, "pizza", 5]
        H2 = [234, "realhastalamuerte", 1]
        H3 = [345, "dbisfun", 10]
        H4 = [456, "lasbestiasdeicom5016", 8]

        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)
        self.data.append(H4)

    def getAllHashtag(self):
        return self.data

    def getHashtagById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getTextByHahtagId(self, id):
        for r in self.data:
            if id == r[0]:
                return r[1]
        return None

    def getFrequencyByHashtagId(self, id):
        for r in self.data:
            if id == r[0]:
                return r[2]
        return None

    def getFrequencyByHashtagText(self, text):
        for r in self.data:
            if text == r[1]:
                return r[2]
        return None