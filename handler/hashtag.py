from flask import jsonify, request
from dao.hashtagDao import HashtagDAO

class HashtagHandler:

    def getAllHashtag(self):
        dao = HashtagDAO()
        result = dao.getAllHashtag()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToHashtagDict(r))
        return jsonify(Hashtag=mapped_result)

    def getAllDistinctHashtag(self):
        dao = HashtagDAO()
        result = dao.getAllDistinctHashtag()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDistinctHashtagDict(r))
        return jsonify(Hashtag=mapped_result)

    def getHashtagByID(self, hash_id):
        dao = HashtagDAO()
        result = dao.getHashtagByID(hash_id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(Hashtag=self.mapToHashtagDict(result))

    def getHashtagByMsgId(self, msg_id):
        dao = HashtagDAO()
        result = dao.getHashtagByMsgId(msg_id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToHashtagDict(r))
        return jsonify(Hashtag=mapped_result)

    def mapToHashtagDict(self, row):
        result = {}
        result["hashtag_id"] = row[0]
        result["hashtag_text"] = row[1]
        return result

    def mapToDistinctHashtagDict(self, row):
        result = {}
        result["hashtag_text"] = row[0]
        return result

    def getMsgsByHashtagText(self, hashtag_text):
        dao = HashtagDAO()
        result = dao.getMsgsByHashtagText(hashtag_text)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Hashtag=mapped_result)

    def getMsgsByChatIdAndHashtagText(self, gchat_id, hashtag_text):
        dao = HashtagDAO()
        result = dao.getMsgsByChatIdAndHashtagText(gchat_id, hashtag_text)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Hashtag=mapped_result)

    def mapToMsgDict(self, row):
        result = {}
        result["message_id"] = row[0]
        result["hashtag_id"] = row[1]
        result["hashtag_text"] = row[2]
        result["message_text"] = row[3]
        result["message_likes"] = row[4]
        result["message_dislikes"] = row[5]
        result["message_date"] = row[6]
        time = "%s:%s:%s" % (row[7].hour, row[7].minute, row[7].second)
        result["time"] = time
        result["person_id"] = row[8]
        result["groupchat_id"] = row[9]
        result["username"] = row[10]
        return result

    def getFrequencyByHashtagText(self, hashtag_text):
        dao = HashtagDAO()
        result = dao.getFrequencyByHashtagText(hashtag_text)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToFrequencyDict(result)
            return jsonify(Hashtag=mapped)

    def mapToFrequencyDict(self, row):
        result = {}
        result["hashtag_text"] = row[0]
        result["frequency"] = row[1]
        return result

    def getTrendingHashtag(self):
        dao = HashtagDAO()
        result = dao.getTrendingHashtag()
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToTrendingDict(r))
        return jsonify(Trending=mapped_result)

    def getTrendingHashtagByGchatId(self, gchat_id):
        dao = HashtagDAO()
        result = dao.getTrendingHashtagByGchatId(gchat_id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToTrendingDict(r))
        return jsonify(Trending=mapped_result)

    def mapToTrendingDict(self, row):
        result = {}
        result["hashtag_text"] = row[0]
        result["frequency"] = row[1]
        return result